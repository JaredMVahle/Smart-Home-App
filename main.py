from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import get_color_from_hex

# Import screen logic
from screens.home.home_screen import HomeScreen
from screens.settings.settings_screen import SettingsScreen
from screens.alarm.alarm_screen import AlarmScreen
from screens.memories.memories_screen import MemoriesScreen
from screens.notes.notes_screen import NotesScreen

class TouchUIApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_selected = "bluegray"
        self.set_theme(self.theme_selected)

    def build(self):
        # Load all .kv files from subfolders
        Builder.load_file("screens/home/home_screen.kv")
        Builder.load_file("screens/settings/settings_screen.kv")
        Builder.load_file("screens/alarm/alarm_screen.kv")
        Builder.load_file("screens/memories/memories_screen.kv")
        Builder.load_file("screens/notes/notes_screen.kv")

        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(AlarmScreen(name="alarm"))
        sm.add_widget(MemoriesScreen(name="memories"))
        sm.add_widget(NotesScreen(name="notes"))
        return sm

    def switch_screen(self, name):
        self.root.current = name

    def set_theme(self, theme):
        self.theme_selected = theme

        if theme == "light":
            self.bg_color = get_color_from_hex("#FFFFFF")
            self.button_color = get_color_from_hex("#4CAF50")
            self.text_color = get_color_from_hex("#222222")
            self.accent_color = get_color_from_hex("#2196F3")

        elif theme == "dark":
            self.bg_color = get_color_from_hex("#212121")
            self.button_color = get_color_from_hex("#424242")
            self.text_color = get_color_from_hex("#FAFAFA")
            self.accent_color = get_color_from_hex("#64FFDA")

        elif theme == "theme2":
            # Umbrion Color Pallet
            self.bg_color = get_color_from_hex("#2F323F")    # Background / Primary
            self.button_color = get_color_from_hex("#64647C")  # Button / Secondary
            self.text_color = get_color_from_hex("#FAFAFA")  # High contrast text
            self.accent_color = get_color_from_hex("#C49F3B")  # Accent (gold)


        elif theme == "theme3":
            # Warm Terracotta Color Pallet 
            #D4272C
            self.bg_color = get_color_from_hex("#cc92c7")    # Pink
            self.button_color = get_color_from_hex("#4cdcc4")  # Teal
            self.text_color = get_color_from_hex("#49454e")  # Greyish
            self.accent_color = get_color_from_hex("#D4272C")  # Redish

        elif theme == "theme4":
            # Cool Ocean Breeze Color Pallet
            self.bg_color = get_color_from_hex("#E0F7F4")    # Background / Primary
            self.button_color = get_color_from_hex("#4CB5AB")  # Button / Secondary
            self.text_color = get_color_from_hex("#2E8C89")  # High contrast text
            self.accent_color = get_color_from_hex("#1C1F1E")  # Accent (gold)

        elif theme == "theme5":
            # Modern Monochrome Color Pallet
            self.bg_color = get_color_from_hex("#1E1E1E")    # Background / Primary
            self.button_color = get_color_from_hex("#3C3C3C")  # Button / Secondary
            self.text_color = get_color_from_hex("#00BFFF")  # High contrast text
            self.accent_color = get_color_from_hex("#FFFFFF")  # Accent (gold)

        else:  # default: bluegray
            self.bg_color = get_color_from_hex("#F0F4F8")
            self.button_color = get_color_from_hex("#3B6978")
            self.text_color = get_color_from_hex("#1E2022")
            self.accent_color = get_color_from_hex("#00BFFF")


        # Hot reload screens with theme applied
        if self.root:
            current_screen = self.root.current
            self.root.clear_widgets()
            self.root.add_widget(HomeScreen(name="home"))
            self.root.add_widget(SettingsScreen(name="settings"))
            self.root.add_widget(AlarmScreen(name="alarm"))
            self.root.add_widget(MemoriesScreen(name="memories"))
            self.root.add_widget(NotesScreen(name="notes"))
            self.root.current = current_screen

if __name__ == "__main__":
    TouchUIApp().run()
