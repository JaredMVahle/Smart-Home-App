from datetime import datetime, timedelta

def now_iso() -> str:
    """
    Returns the current timestamp in ISO 8601 format.

    Example: '2025-06-07T19:30:15'
    """
    return datetime.now().isoformat(timespec="seconds")

def now_compact() -> str:
    """
    Returns the current timestamp formatted for file-safe names.

    Example: '20250607_193015'
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def format_friendly(dt: datetime) -> str:
    """
    Converts a datetime object into a human-friendly string.

    Example: 'June 7, 2025 at 7:30 PM'
    """
    return dt.strftime("%B %-d, %Y at %-I:%M %p")

def parse_iso(date_str: str) -> datetime:
    """
    Converts an ISO 8601 string back to a datetime object.

    Returns:
    - datetime: Parsed datetime object.
    - If parsing fails, returns the current datetime.
    """
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        return datetime.now()

def time_ago(dt: datetime, reference: datetime = None) -> str:
    """
    Returns a relative time difference between `dt` and now.

    Example: '2 hours ago', '5 minutes ago', 'just now'
    """
    if reference is None:
        reference = datetime.now()
    delta = reference - dt

    seconds = int(delta.total_seconds())
    minutes = seconds // 60
    hours = minutes // 60
    days = delta.days

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    else:
        return f"{days} day{'s' if days != 1 else ''} ago"

def add_minutes(base_time: datetime, minutes: int) -> datetime:
    """
    Adds a number of minutes to a datetime object.

    Useful for alarm or timer setup.

    Returns:
    - datetime: The adjusted time.
    """
    return base_time + timedelta(minutes=minutes)