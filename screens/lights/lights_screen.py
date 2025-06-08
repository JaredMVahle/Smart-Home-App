from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDSwitch

from utils.color_utils import ColorPicker

class LightsScreen(MDScreen):
    selected_room = None

    def select_room(self, room_name, state):
        if state != "down":
            return
        self.selected_room = room_name
        self.show_controls()

    def show_controls(self):
        panel = self.ids.control_panel
        panel.clear_widgets()

        # Power Toggle
        power_row = MDBoxLayout(orientation="horizontal", spacing="12dp", size_hint_y=None, height="48dp")
        power_row.add_widget(MDLabel(text="Power", halign="left", theme_text_color="Custom", text_color=self.theme_cls.primary_color))
        power_switch = MDSwitch()
        power_switch.bind(active=lambda instance, value: self.toggle_power(value))
        power_row.add_widget(power_switch)
        panel.add_widget(power_row)

        # Brightness Slider
        panel.add_widget(MDLabel(text="Brightness", halign="left", theme_text_color="Custom", text_color=self.theme_cls.primary_color))
        brightness_slider = MDSlider(min=0, max=100, value=50)
        brightness_slider.bind(value=self.set_brightness)
        panel.add_widget(brightness_slider)

        # Color Picker Button
        color_button = MDRaisedButton(text="Choose Light Color", md_bg_color=self.theme_cls.accent_color)
        color_button.bind(on_release=self.open_color_picker)
        panel.add_widget(color_button)

    def toggle_power(self, is_on):
        print(f"Power {'ON' if is_on else 'OFF'} for {self.selected_room}")

    def set_brightness(self, instance, value):
        print(f"Brightness set to {int(value)}% in {self.selected_room}")

    def open_color_picker(self, *args):
        picker = ColorPicker()
        picker.open()
        picker.bind(on_select_color=lambda instance, color: self.set_color(color))

    def set_color(self, color):
        print(f"Color set to {color} in {self.selected_room}")
