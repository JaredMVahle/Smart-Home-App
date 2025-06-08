from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.app import App
from functools import partial

from utils.color_utils import hex_to_rgba
from utils.log_utils import (
    debug_log,
    enable_logging,
    disable_logging,
    is_logging_enabled,
)
from utils.file_utils import save_json, load_json, get_app_data_path


PREF_PATH = get_app_data_path("user_prefs.json")

THEMES = {
    "default": {
        "name": "default",
        "bg_color": "#F0F4F8",
        "button_color": "#3B6978",
        "text_color": "#1E2022",
        "accent_color": "#00BFFF",
    },
    "pikachu": {
        "name": "pikachu",
        "bg_color": "#FFF176",
        "button_color": "#F57C00",
        "text_color": "#212121",
        "accent_color": "#FFEB3B",
    },
    "charizard": {
        "name": "charizard",
        "bg_color": "#FF7043",
        "button_color": "#BF360C",
        "text_color": "#FFFFFF",
        "accent_color": "#F4511E",
    },
    "bulbasaur": {
        "name": "bulbasaur",
        "bg_color": "#A5D6A7",
        "button_color": "#66BB6A",
        "text_color": "#1B5E20",
        "accent_color": "#388E3C",
    },
    "squirtle": {
        "name": "squirtle",
        "bg_color": "#81D4FA",
        "button_color": "#0288D1",
        "text_color": "#0D47A1",
        "accent_color": "#00ACC1",
    },
    "mewtwo": {
        "name": "mewtwo",
        "bg_color": "#CE93D8",
        "button_color": "#7B1FA2",
        "text_color": "#311B92",
        "accent_color": "#9575CD",
    },
    "umbreon": {
        "name": "umbreon",
        "bg_color": "#2F323F",
        "button_color": "#64647C",
        "text_color": "#FAFAFA",
        "accent_color": "#FFD700",
    },
    "sylveon": {
        "name": "sylveon",
        "bg_color": "#FDE1F3",
        "button_color": "#9CC2E5",
        "text_color": "#6E4D6A",
        "accent_color": "#FF84A1",
    },
    "lucario": {
        "name": "lucario",
        "bg_color": "#2B3C50",
        "button_color": "#AAB7BD",
        "text_color": "#FFFFFF",
        "accent_color": "#519ABA",
    },
    "garchomp": {
        "name": "garchomp",
        "bg_color": "#4C3F91",
        "button_color": "#E15F41",
        "text_color": "#FFFFFF",
        "accent_color": "#FDB833",
    },
    "venusaur": {
        "name": "venusaur",
        "bg_color": "#9BCCB7",
        "button_color": "#E06D6D",
        "text_color": "#2A3B36",
        "accent_color": "#71B48D",
    },
}


class SettingsScreen(MDScreen):

    def on_kv_post(self, base_widget):
        try:
            debug_log("SettingsScreen on_kv_post called")
            self.load_theme_cards()
            self.load_user_preferences()
        except Exception as e:
            import traceback
            traceback.print_exc()
            debug_log(f"ERROR in on_kv_post: {e}")

    def load_theme_cards(self):
        row = self.ids.theme_row
        row.clear_widgets()
        app = App.get_running_app()
        debug_log("Generating theme cards")

        for theme_name, colors in THEMES.items():
            debug_log(f"Adding card for theme: {theme_name}")
            bg = hex_to_rgba(colors["bg_color"])
            button = hex_to_rgba(colors["button_color"])
            text = hex_to_rgba(colors["text_color"])
            accent = hex_to_rgba(colors["accent_color"])

            is_selected = app.current_theme_name == colors["name"]

            card = MDCard(
                size_hint=(None, None),
                size=("100dp", "100dp"),
                md_bg_color=bg,
                radius=[16],
                padding="8dp",
                orientation="vertical",
                spacing="6dp",
                elevation=12 if is_selected else 4,
                on_release=partial(self._on_theme_selected, colors)
            )
            card.bind(size=self._keep_square)

            card.add_widget(MDLabel(
                text=theme_name.capitalize(),
                halign="center",
                theme_text_color="Custom",
                text_color=text
            ))

            for color in (button, text, accent):
                bar = Widget(size_hint_y=None, height="8dp")
                with bar.canvas.before:
                    Color(rgba=color)
                    bar.rect = Rectangle()
                    bar.bind(size=self._update_rect, pos=self._update_rect)
                card.add_widget(bar)

            wrapper = BoxLayout(size_hint=(None, None), padding=0)
            wrapper.size = card.size
            wrapper.add_widget(card)
            card.bind(size=lambda inst, val: setattr(wrapper, 'size', val))

            if is_selected:
                with wrapper.canvas.before:
                    Color(0.8, 0.8, 0.8, 1)
                    wrapper.border = Rectangle(pos=wrapper.pos, size=wrapper.size)
                    Color(1, 1, 1, 0.12)
                    wrapper.glow = Rectangle(pos=(wrapper.x - 5, wrapper.y - 5), size=(wrapper.width + 10, wrapper.height + 10))
                wrapper.bind(pos=self._update_wrapper_graphics, size=self._update_wrapper_graphics)

            row.add_widget(wrapper)

    def _on_theme_selected(self, theme: dict, *args):
        debug_log(f"Theme selected: {theme['name']}")
        App.get_running_app().set_theme_direct(theme)
        self.save_user_preferences()

    def toggle_logging(self, state: bool):
        if state:
            enable_logging()
        else:
            disable_logging()
        debug_log(f"Logging toggled {'on' if state else 'off'}")
        self.save_user_preferences()

    def save_user_preferences(self):
        app = App.get_running_app()
        prefs = {
            "theme": app.current_theme_name,
            "logging": is_logging_enabled()
        }
        save_json(PREF_PATH, prefs)
        debug_log("User preferences saved")

    def load_user_preferences(self):
        prefs = load_json(PREF_PATH, fallback={})
        app = App.get_running_app()

        theme_name = prefs.get("theme", "default")
        theme = THEMES.get(theme_name, THEMES["default"])
        app.set_theme_direct(theme)
        debug_log(f"Restored theme: {theme_name}")

        logging_enabled = prefs.get("logging", True)
        self.ids.log_toggle.active = logging_enabled
        if logging_enabled:
            enable_logging()
        else:
            disable_logging()
        debug_log(f"Restored logging preference: {logging_enabled}")

    def _keep_square(self, instance, *_):
        instance.height = instance.width

    def _update_rect(self, instance, *_):
        instance.canvas.before.children[-1].size = instance.size
        instance.canvas.before.children[-1].pos = instance.pos

    def _update_wrapper_graphics(self, instance, *_):
        if hasattr(instance, "border"):
            instance.border.pos = instance.pos
            instance.border.size = instance.size
        if hasattr(instance, "glow"):
            instance.glow.pos = (instance.x - 5, instance.y - 5)
            instance.glow.size = (instance.width + 10, instance.height + 10)
