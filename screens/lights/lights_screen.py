from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty, NumericProperty

class LightsScreen(MDScreen):
    selected_room = StringProperty("")
    light_on = BooleanProperty(False)
    brightness = NumericProperty(50)
    hue = NumericProperty(0)

    def handle_room_selection(self, room):
        self.selected_room = room

    def toggle_light(self, switch_state):
        self.light_on = switch_state

    def on_brightness_change(self, slider, value):
        self.brightness = value

    def on_color_change(self, slider, value):
        self.hue = value
