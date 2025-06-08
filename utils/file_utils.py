import os
import json
from pathlib import Path

def ensure_directory(path: str) -> None:
    """
    Ensure the directory exists for the given path.
    If the path is a file, its parent directory is used.
    """
    directory = Path(path).parent
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

def save_json(path: str, data: dict, indent: int = 4) -> bool:
    """
    Save a dictionary to a file as JSON. Ensures the directory exists.

    Parameters:
    - path (str): File path to write to.
    - data (dict): The data to save.
    - indent (int): Indentation level for readability.

    Returns:
    - bool: True if saved successfully, False on error.
    """
    try:
        ensure_directory(path)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent)
        return True
    except Exception as e:
        print(f"[file_utils] Failed to save JSON to {path}: {e}")
        return False

def load_json(path: str, fallback: dict = None) -> dict:
    """
    Load a JSON file and return its contents as a dictionary.

    Parameters:
    - path (str): File path to load.
    - fallback (dict): Default return if file not found or fails.

    Returns:
    - dict: Loaded data or fallback.
    """
    if fallback is None:
        fallback = {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return fallback
    except Exception as e:
        print(f"[file_utils] Failed to load JSON from {path}: {e}")
        return fallback

def file_exists(path: str) -> bool:
    """
    Check whether a file exists.

    Parameters:
    - path (str): The file path to check.

    Returns:
    - bool: True if file exists, else False.
    """
    return Path(path).is_file()

def read_text(path: str, fallback: str = "") -> str:
    """
    Read plain text from a file.

    Parameters:
    - path (str): The file path.
    - fallback (str): Return this if file not found or fails.

    Returns:
    - str: File contents or fallback.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[file_utils] Failed to read text from {path}: {e}")
        return fallback

def write_text(path: str, text: str) -> bool:
    """
    Write plain text to a file, replacing its contents.

    Parameters:
    - path (str): File path to write.
    - text (str): The text content.

    Returns:
    - bool: True on success, False on error.
    """
    try:
        ensure_directory(path)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    except Exception as e:
        print(f"[file_utils] Failed to write text to {path}: {e}")
        return False

def get_app_data_path(filename: str) -> str:
    """
    Get the recommended path for saving user data/configs in a cross-platform way.

    Parameters:
    - filename (str): The file name (not full path).

    Returns:
    - str: Absolute path in the user’s home directory or config folder.
    """
    base = Path.home() / ".smart_home_app"
    return str(base / filename)