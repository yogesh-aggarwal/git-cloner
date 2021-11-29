import os
import socket
import subprocess


def run_command(command: str) -> None:
    os.system(command)


def get_command_output_when_complete(command: str) -> str:
    return subprocess.getoutput(command)


def check_if_git_installed() -> bool:
    return get_command_output_when_complete("git").startswith("usage")


def check_internet() -> bool:
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=10)
        return True
    except Exception:
        return False
