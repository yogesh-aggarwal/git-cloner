def no_git_installed():
    raise RuntimeError("No git installed! Get it here: https://git-scm.com/")


def no_internet_connection():
    raise RuntimeError(
        "No internet connection! Make sure to have a stable internet connection"
    )
