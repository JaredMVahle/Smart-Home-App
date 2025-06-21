import sys
import os
from datetime import datetime
from pathlib import Path

# Define base directory relative to this file
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / ".smart_home_app" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOG_DIR / f"startup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

def log(msg):
    print(msg)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def main():
    try:
        from main import TouchUIApp
        log("[INFO] Launching TouchUIApp...")
        TouchUIApp().run()

    except ModuleNotFoundError as e:
        log(f"[ERROR] Missing dependency: {e.name}")
        log("Try running: pip install -r requirements.txt")

    except Exception as ex:
        import traceback
        log("[FATAL ERROR] App crashed at runtime:")
        log(traceback.format_exc())


if __name__ == "__main__":
    main()
