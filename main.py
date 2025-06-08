# Imports section
import os
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ColorProperty

from utils.theme_utils import apply_theme_to_app
from utils.log_utils import debug_log
from utils.file_utils import load_json, get_app_data_path

from screens.settings.settings_screen import THEMES,  SettingsScreen
from screens.home.home_screen import HomeScreen
from screens.alarm.alarm_screen import AlarmScreen
from screens.memories.memories_screen import MemoriesScreen
from screens.notes.notes_screen import NotesScreen

#Function/Class Section
class TouchUIApp(MDApp):
    bg_color = ColorProperty()
    button_color = ColorProperty()
    text_color = ColorProperty()
    accent_color = ColorProperty()
    current_theme_name = "default"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pref_path = get_app_data_path("user_prefs.json")
        prefs = load_json(pref_path, fallback={})
        theme_name = prefs.get("theme", "default")
        theme = THEMES.get(theme_name, THEMES["default"])
        apply_theme_to_app(self, theme)

    def build(self):
        try:
            base_dir = os.path.dirname(__file__)
            debug_log("[BUILD] Loading KV files")

            Builder.load_file(os.path.join(base_dir, "screens/home/home_screen.kv"))
            Builder.load_file(os.path.join(base_dir, "screens/settings/settings_screen.kv"))
            Builder.load_file(os.path.join(base_dir, "screens/alarm/alarm_screen.kv"))
            Builder.load_file(os.path.join(base_dir, "screens/memories/memories_screen.kv"))
            Builder.load_file(os.path.join(base_dir, "screens/notes/notes_screen.kv"))

            debug_log("[BUILD] Initializing screens")
            self.sm = ScreenManager()
            self.sm.add_widget(HomeScreen(name="home"))
            self.sm.add_widget(SettingsScreen(name="settings"))
            self.sm.add_widget(AlarmScreen(name="alarm"))
            self.sm.add_widget(MemoriesScreen(name="memories"))
            self.sm.add_widget(NotesScreen(name="notes"))

            debug_log("[BUILD] Build complete, returning root")
            return self.sm

        except Exception as e:
            import traceback
            print("[FATAL BUILD ERROR]")
            traceback.print_exc()
            return None

    def switch_screen(self, name):
        debug_log(f"Switching screen to: {name}")
        self.root.current = name

    def set_theme_direct(self, theme: dict, *args):
        debug_log(f"Applying theme: {theme.get('name', 'unknown')}")
        apply_theme_to_app(self, theme)
        self.update_screen_colors()

    def update_screen_colors(self):
        debug_log("Propagating theme updates to all screens")
        if self.root:
            for screen in self.root.screens:
                if hasattr(screen, "update_colors") and callable(screen.update_colors):
                    screen.update_colors()
