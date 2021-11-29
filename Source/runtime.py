import git
import utils
import errors


def setup():
    if not utils.check_if_git_installed():
        errors.no_git_installed()
    if not utils.check_internet():
        errors.no_internet_connection()


def main():
    setup()
    # git.fetch_repos([
    #     git.Repository("yogesh-aggarwal", "fanatic-data-backend"),
    #     git.Repository("yogesh-aggarwal", "fanatic-data-backend")
    # ])
    git.fetch_by_languages("yogesh-aggarwal", ["python"], plain_tree=False)


if __name__ == "__main__":
    main()
