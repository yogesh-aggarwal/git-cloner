import socket
import subprocess


def check_if_git_installed() -> bool:
    return subprocess.getoutput('git').startswith("usage")


def check_internet() -> bool:
    try:
        socket.create_connection(("1.2.1.1", 53), timeout=10)
        return True
    except Exception:
        return False
