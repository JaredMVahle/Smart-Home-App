from utils.color_utils import parse_color


def apply_theme_to_app(app, theme: dict):
    """
    Applies a theme dictionary to the app's global color properties.

    Parameters:
    - app: The MDApp or subclass (e.g. TouchUIApp).
    - theme (dict): Contains 'bg_color', 'button_color', 'text_color', 'accent_color', 'name'.
    """
    app.bg_color = parse_color(theme.get("bg_color", "#FFFFFF"))
    app.button_color = parse_color(theme.get("button_color", "#CCCCCC"))
    app.text_color = parse_color(theme.get("text_color", "#000000"))
    app.accent_color = parse_color(theme.get("accent_color", "#FF0000"))
    app.current_theme_name = theme.get("name", "default")


def add_theme_name(theme_dict: dict, name: str) -> dict:
    """
    Returns a copy of the given theme dictionary with a 'name' key added.

    Useful for programmatically assigning names to JSON-based or dynamically generated themes.
    """
    theme = theme_dict.copy()
    theme["name"] = name
    return theme


def get_theme_names(theme_collection: dict) -> list:
    """
    Returns a sorted list of all theme names in a given THEMES dictionary.

    Parameters:
    - theme_collection (dict): A dictionary of theme name → theme dict

    Returns:
    - List[str]: Alphabetically sorted theme names
    """
    return sorted(theme_collection.keys())
