import subprocess


def check_if_git_installed() -> bool:
    return subprocess.getoutput('git').startswith("usage")
