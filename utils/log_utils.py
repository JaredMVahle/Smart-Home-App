import os
from datetime import datetime
from utils.file_utils import ensure_directory, get_app_data_path

# Toggleable flag
LOGGING_ENABLED = True

# Path to store logs
LOG_FOLDER = get_app_data_path("logs")
ensure_directory(os.path.join(LOG_FOLDER, "temp.txt"))

# Generate timestamped log file
def _get_log_path() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(LOG_FOLDER, f"log_{timestamp}.txt")

# Global log path (rotates once per run)
LOG_FILE = _get_log_path()


def debug_log(message: str, print_also: bool = True):
    """
    Logs a message to the current session log file, with a timestamp.

    Parameters:
    - message (str): The message to log
    - print_also (bool): Whether to also print to stdout
    """
    if not LOGGING_ENABLED:
        return

    timestamp = datetime.now().strftime("[%H:%M:%S]")
    line = f"{timestamp} {message}"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception as e:
        print(f"[log_utils] Failed to write log: {e}")

    if print_also:
        print(line)


def enable_logging():
    global LOGGING_ENABLED
    LOGGING_ENABLED = True
    debug_log("Logging ENABLED")


def disable_logging():
    global LOGGING_ENABLED
    debug_log("Logging DISABLED")
    LOGGING_ENABLED = False


def is_logging_enabled() -> bool:
    return LOGGING_ENABLED
