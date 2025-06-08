from kivy.metrics import dp
from kivy.core.window import Window

def aspect_ratio(width: float, height: float) -> float:
    """
    Returns the aspect ratio (width divided by height).

    Example: 16:9 = 1.78
    """
    if height == 0:
        return 1
    return round(width / height, 2)

def get_window_aspect_ratio() -> float:
    """
    Returns the current window's aspect ratio.
    Useful for responsive layout decisions.
    """
    return aspect_ratio(Window.width, Window.height)

def square_size_from_width(width_dp: float) -> tuple:
    """
    Given a desired width in dp, return a (width, height) pair with a 1:1 ratio.
    Useful for cards, images, or tiles.
    """
    size = dp(width_dp)
    return (size, size)

def get_responsive_columns(min_card_width_dp: int = 120) -> int:
    """
    Determines how many columns can fit on screen based on a minimum width.

    Parameters:
    - min_card_width_dp (int): Minimum card width in dp (default 120dp)

    Returns:
    - int: Column count that will fit horizontally
    """
    screen_width = Window.width
    card_width = dp(min_card_width_dp)
    return max(1, int(screen_width / card_width))

def clamp(min_value, value, max_value):
    """
    Clamps a value between a minimum and maximum bound.

    Example:
    clamp(1, 5, 10) => 5
    clamp(1, 0, 10) => 1
    """
    return max(min_value, min(value, max_value))