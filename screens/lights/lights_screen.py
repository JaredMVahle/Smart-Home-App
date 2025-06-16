from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, BooleanProperty, NumericProperty


class LightsScreen(MDScreen):
    selected_room = StringProperty("")
    light_on = BooleanProperty(False)
    brightness = NumericProperty(50)
    hue = NumericProperty(0)

    def handle_room_selection(self, room):
        self.selected_room = room
        print(f"Room selected: {room}")

    def toggle_light(self, instance, value):
        self.light_on = value
        print(f"Light {'ON' if value else 'OFF'} in {self.selected_room}")

    def on_brightness_change(self, instance, value):
        self.brightness = value
        print(f"Brightness set to {int(value)}% in {self.selected_room}")

    def on_color_change(self, instance, value):
        self.hue = value
        print(f"Hue set to {int(value)}° in {self.selected_room}")