from kivy.utils import get_color_from_hex


def is_valid_hex(hex_color: str) -> bool:
    """
    Validates whether the provided string is a proper hex color.

    Supports shorthand (#FFF) or full hex (#FFFFFF).

    Parameters:
    - hex_color (str): The hex string to check.

    Returns:
    - bool: True if valid, False otherwise.
    """
    if not isinstance(hex_color, str) or not hex_color.startswith("#"):
        return False
    hex_len = len(hex_color)
    return hex_len in {4, 7} and all(c in "0123456789ABCDEFabcdef" for c in hex_color[1:])


def hex_to_rgba(hex_color: str) -> tuple:
    """
    Converts a hex color string to a normalized (R, G, B, A) tuple.

    Example: '#FFAA00' -> (1.0, 0.666, 0.0, 1)

    Parameters:
    - hex_color (str): A hex color like '#FFAABB'

    Returns:
    - tuple: RGBA color in normalized 0-1 float format
    """
    hex_color = hex_color.lstrip("#")
    lv = len(hex_color)
    rgb = tuple(int(hex_color[i:i + lv // 3], 16) / 255 for i in range(0, lv, lv // 3))
    return (*rgb, 1)


def parse_color(hex_val: str) -> tuple:
    """
    Parses a hex color string into RGBA, with fallback safety.

    If the input is invalid or malformed, returns white (1, 1, 1, 1).

    Parameters:
    - hex_val (str): A hex color code like '#F0F4F8'

    Returns:
    - tuple: Normalized RGBA color
    """
    if is_valid_hex(hex_val):
        return get_color_from_hex(hex_val)
    return (1, 1, 1, 1)
