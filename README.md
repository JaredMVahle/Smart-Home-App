# 🏠 Smart-Home-App

**Smart-Home-App** is a modular, touchscreen-friendly smart home interface built using Python, Kivy, and KivyMD. Designed with scalability and clarity in mind, this app provides a beautiful, themeable UI to manage different aspects of your home life — alarms, notes, memories, and more — all on a Raspberry Pi or embedded touchscreen panel.

---

## 🚀 Features

- 🏠 **Home Screen**: Central navigation hub
- **Security**: Connect to IP cameras or Ring for live feeds
- **Weather**: Fetch current conditions based on home location (shown on Home Screen)
- **Journaling**: Daily logging feature with NLP sentiment analysis for mood detection
- ⚙️ **Settings Screen**: Supports dynamic theme switching with 6 built-in palettes
- ⏰ **Alarm Module**: Framework to schedule and display alarms
- 📝 **Notes Module**: Create and manage simple text notes
- 📸 **Memories Module**: Placeholder for media/gallery integration
- 🎨 **Custom Themes**: Choose from Light, Dark, Umbrion, Terracotta, Ocean Breeze, and Monochrome
- 📱 **Touchscreen Optimized**: Designed with material components and full-screen layouts
- **Package Tracker**: View real-time delivery info for incoming packages
- **Smart Timers**: Add quick-start timers for laundry, sleep reminders, etc.
- **Network Scanner**: Show currently connected devices and basic diagnostics in Settings
- **Lighting**: Smoother per-room management with fade options and easy save

## 🧠 Architecture Overview

```plaintext
Smart-Home-App/
├── main.py                         # Entry point and theme logic
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git exclusions
├── README.md                       # Project documentation
├── screens/
│   ├── home/
│   │   ├── home_screen.py
│   │   └── home_screen.kv
│   ├── settings/
│   │   ├── settings_screen.py
│   │   └── settings_screen.kv
│   ├── alarm/
        ├── alarm_screen.py
│   │   └── alarm_screen.kv
│   ├── notes/
        ├── notes_screen.py
│   │   └── notes_screen.kv
│   └── memories/
        ├── memories_screen.py
│   │   └── memories_screen.kv
```
