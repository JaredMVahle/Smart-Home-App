from math import cos, sin, pi, sqrt, atan
from colorsys import rgb_to_hsv, hsv_to_rgb

from kivy.clock import Clock
from kivy.graphics import Mesh, InstructionGroup, Color
from kivy.logger import Logger
from kivy.properties import NumericProperty, BoundedNumericProperty, ListProperty, ObjectProperty, ReferenceListProperty, StringProperty, AliasProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex, get_hex_from_color

__all__ = ('ColorPicker', 'ColorWheel')

# Helper functions
def distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0]) ** 2. + (pt1[1] - pt2[1]) ** 2.)

def polar_to_rect(origin, r, theta):
    return origin[0] + r * cos(theta), origin[1] + r * sin(theta)

def rect_to_polar(origin, x, y):
    if x == origin[0]:
        if y == origin[1]:
            return 0, 0
        elif y > origin[1]:
            return y - origin[1], pi / 2
        else:
            return origin[1] - y, 3 * pi / 2
    t = atan(float((y - origin[1])) / (x - origin[0]))
    if x - origin[0] < 0:
        t += pi
    if t < 0:
        t += 2 * pi
    return distance((x, y), origin), t

# Core visual class
class _ColorArc(InstructionGroup):
    def __init__(self, r_min, r_max, theta_min, theta_max,
                 color=(0, 0, 1, 1), origin=(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.origin = origin
        self.r_min = r_min
        self.r_max = r_max
        self.theta_min = theta_min
        self.theta_max = theta_max
        self.color = color
        self.color_instr = Color(*color, mode='hsv')
        self.add(self.color_instr)
        self.mesh = self.get_mesh()
        self.add(self.mesh)

    def get_mesh(self):
        v = []
        theta_step_outer = 0.1
        theta = self.theta_max - self.theta_min
        d_outer = int(theta / theta_step_outer)
        theta_step_outer = theta / d_outer
        if self.r_min == 0:
            for x in range(0, d_outer, 2):
                v += polar_to_rect(self.origin, self.r_max, self.theta_min + x * theta_step_outer) * 2
                v += polar_to_rect(self.origin, 0, 0) * 2
                v += polar_to_rect(self.origin, self.r_max, self.theta_min + (x + 1) * theta_step_outer) * 2
            if not d_outer & 1:
                v += polar_to_rect(self.origin, self.r_max, self.theta_min + d_outer * theta_step_outer) * 2
        else:
            for x in range(d_outer + 1):
                v += polar_to_rect(self.origin, self.r_min, self.theta_min + x * theta_step_outer) * 2
                v += polar_to_rect(self.origin, self.r_max, self.theta_min + x * theta_step_outer) * 2
        return Mesh(vertices=v, indices=list(range(int(len(v) / 4))), mode='triangle_strip')

    def change_color(self, color=None, color_delta=None, sv=None, a=None):
        self.remove(self.color_instr)
        if color is not None:
            self.color = color
        elif color_delta is not None:
            self.color = [self.color[i] + color_delta[i] for i in range(4)]
        elif sv is not None:
            self.color = (self.color[0], sv[0], sv[1], self.color[3])
        elif a is not None:
            self.color = (self.color[0], self.color[1], self.color[2], a)
        self.color_instr = Color(*self.color, mode='hsv')
        self.insert(0, self.color_instr)

# Color wheel logic
class ColorWheel(Widget):
    r = BoundedNumericProperty(0, min=0, max=1)
    g = BoundedNumericProperty(0, min=0, max=1)
    b = BoundedNumericProperty(0, min=0, max=1)
    a = BoundedNumericProperty(0, min=0, max=1)
    color = ReferenceListProperty(r, g, b, a)

    _origin = ListProperty((100, 100))
    _radius = NumericProperty(100)
    _piece_divisions = NumericProperty(10)
    _pieces_of_pie = NumericProperty(16)

    def __init__(self, **kwargs):
        self.arcs = []
        self.sv_idx = 0
        self._inertia_slowdown = 1.25
        self._inertia_cutoff = .25
        self._num_touches = 0
        self._pinch_flag = False
        pdv = self._piece_divisions
        self.sv_s = [(float(x) / pdv, 1) for x in range(pdv)] + [(1, float(y) / pdv) for y in reversed(range(pdv))]
        super().__init__(**kwargs)

    def _reset_canvas(self):
        self.canvas.clear()
        self.arcs = []
        self.sv_idx = 0
        pdv = self._piece_divisions
        ppie = self._pieces_of_pie
        for r in range(pdv):
            for t in range(ppie):
                self.arcs.append(_ColorArc(
                    self._radius * (float(r) / pdv),
                    self._radius * (float(r + 1) / pdv),
                    2 * pi * (float(t) / ppie),
                    2 * pi * (float(t + 1) / ppie),
                    origin=self._origin,
                    color=(float(t) / ppie, self.sv_s[self.sv_idx + r][0], self.sv_s[self.sv_idx + r][1], 1)
                ))
                self.canvas.add(self.arcs[-1])

    def on__origin(self, *_): self._reset_canvas()
    def on__radius(self, *_): self._reset_canvas()

    def recolor_wheel(self):
        ppie = self._pieces_of_pie
        for idx, segment in enumerate(self.arcs):
            segment.change_color(sv=self.sv_s[int(self.sv_idx + idx / ppie)])

    def on_touch_up(self, touch):
        if touch.grab_current is not self: return
        touch.ungrab(self)
        self._num_touches -= 1
        if not self._pinch_flag:
            r, theta = rect_to_polar(self._origin, *touch.pos)
            if r >= self._radius: return
            piece = int((theta / (2 * pi)) * self._pieces_of_pie)
            division = int((r / self._radius) * self._piece_divisions)
            hsva = list(self.arcs[self._pieces_of_pie * division + piece].color)
            self.color = list(hsv_to_rgb(*hsva[:3])) + hsva[-1:]

# ColorPicker logic
class ColorPicker(RelativeLayout):
    font_name = StringProperty('data/fonts/RobotoMono-Regular.ttf')
    color = ListProperty((1, 1, 1, 1))
    wheel = ObjectProperty(None)
    foreground_color = ListProperty((1, 1, 1, 1))
    _update_clr_ev = _update_hex_ev = None

    def __init__(self, **kwargs):
        self._updating_clr = False
        super().__init__(**kwargs)

    def set_color(self, color):
        self._updating_clr = True
        if len(color) == 3:
            self.color[:3] = color
        else:
            self.color = color
        self._updating_clr = False

    def _get_hsv(self): return rgb_to_hsv(*self.color[:3])
    def _set_hsv(self, value):
        if self._updating_clr: return
        self.set_color(value)
    hsv = AliasProperty(_get_hsv, _set_hsv, bind=('color',))

    def _get_hex(self): return get_hex_from_color(self.color)
    def _set_hex(self, value):
        if self._updating_clr: return
        self.set_color(get_color_from_hex(value)[:4])
    hex_color = AliasProperty(_get_hex, _set_hex, bind=('color',), cache=True)

def is_valid_hex(hex_color: str) -> bool:
    """
    Validates whether the provided string is a proper hex color.

    Supports shorthand (#FFF) or full hex (#FFFFFF).

    Parameters:
    - hex_color (str): The hex string to check.

    Returns:
    - bool: True if valid, False otherwise.
    """
    if not isinstance(hex_color, str) or not hex_color.startswith("#"):
        return False
    hex_len = len(hex_color)
    return hex_len in {4, 7} and all(c in "0123456789ABCDEFabcdef" for c in hex_color[1:])


def hex_to_rgba(hex_color: str) -> tuple:
    """
    Converts a hex color string to a normalized (R, G, B, A) tuple.

    Example: '#FFAA00' -> (1.0, 0.666, 0.0, 1)

    Parameters:
    - hex_color (str): A hex color like '#FFAABB'

    Returns:
    - tuple: RGBA color in normalized 0-1 float format
    """
    hex_color = hex_color.lstrip("#")
    lv = len(hex_color)
    rgb = tuple(int(hex_color[i:i + lv // 3], 16) / 255 for i in range(0, lv, lv // 3))
    return (*rgb, 1)


def parse_color(hex_val: str) -> tuple:
    """
    Parses a hex color string into RGBA, with fallback safety.

    If the input is invalid or malformed, returns white (1, 1, 1, 1).

    Parameters:
    - hex_val (str): A hex color code like '#F0F4F8'

    Returns:
    - tuple: Normalized RGBA color
    """
    if is_valid_hex(hex_val):
        return get_color_from_hex(hex_val)
    return (1, 1, 1, 1)
