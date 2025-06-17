from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from utils.style_constants import SELECTED_BUTTON_BG
from utils.file_utils import load_json, save_json, get_app_data_path

class AlarmScreen(MDScreen):
    selected_room = StringProperty("Bedroom")  # Default
    light_on = BooleanProperty(False)
    brightness = NumericProperty(50)
    hue = NumericProperty(0)
    selected_bg_color = ListProperty(SELECTED_BUTTON_BG)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._prefs_path = get_app_data_path("user_prefs.json")
        self._load_state()

    def _load_state(self):
        prefs = load_json(self._prefs_path, fallback={})
        room_data = prefs.get("light_state", {}).get(self.selected_room, {})
        self.light_on = room_data.get("on", False)
        self.brightness = room_data.get("brightness", 50)
        self.hue = room_data.get("hue", 0)

    def _save_state(self):
        prefs = load_json(self._prefs_path, fallback={})
        if "light_state" not in prefs:
            prefs["light_state"] = {}

        prefs["light_state"][self.selected_room] = {
            "on": self.light_on,
            "brightness": self.brightness,
            "hue": self.hue
        }

        save_json(self._prefs_path, prefs)

    def handle_room_selection(self, room):
        self._save_state()  # Save current room before switching
        self.selected_room = room
        self._load_state()
        print(f"Switched to room: {room}")

    def toggle_light(self, instance, value):
        self.light_on = value
        print(f"Light {'ON' if value else 'OFF'} in {self.selected_room}")
        self._save_state()

    def on_brightness_change(self, instance, value):
        self.brightness = value
        print(f"Brightness set to {int(value)}% in {self.selected_room}")
        self._save_state()

    def on_color_change(self, instance, value):
        self.hue = value
        print(f"Hue set to {int(value)}° in {self.selected_room}")
        self._save_state()