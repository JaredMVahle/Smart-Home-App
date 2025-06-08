import socket
import platform
import subprocess

def is_online(host: str = "8.8.8.8", port: int = 53, timeout: float = 2.0) -> bool:
    """
    Returns True if the internet is reachable via socket connection.

    Default host is Google DNS at 8.8.8.8 (TCP/UDP port 53).

    Parameters:
    - host (str): Host to attempt connection to.
    - port (int): Port number (default: 53).
    - timeout (float): Connection timeout in seconds.

    Returns:
    - bool: True if connection succeeds, else False.
    """
    try:
        socket.setdefaulttimeout(timeout)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
        return True
    except Exception:
        return False

def ping_device(host: str, count: int = 1) -> bool:
    """
    Pings a local or remote device.

    Parameters:
    - host (str): IP address or hostname of the device.
    - count (int): Number of ping attempts.

    Returns:
    - bool: True if ping is successful, else False.
    """
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        result = subprocess.run(
            ["ping", param, str(count), host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

def get_local_ip() -> str:
    """
    Returns the current device's local IP address (e.g. '192.168.x.x').

    Falls back to '127.0.0.1' if detection fails.

    Returns:
    - str: Local IPv4 address.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Doesn't actually send
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

def resolve_hostname(hostname: str) -> str:
    """
    Resolves a hostname to an IP address.

    Parameters:
    - hostname (str): e.g., 'raspberrypi.local'

    Returns:
    - str: Resolved IP or fallback to '127.0.0.1'
    """
    try:
        return socket.gethostbyname(hostname)
    except Exception:
        return "127.0.0.1"