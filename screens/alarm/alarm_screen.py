from kivymd.uix.screen import MDScreen

class AlarmScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("📟 AlarmScreen loaded")
