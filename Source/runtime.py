import git
import click
import utils
import errors


def setup():
    if not utils.check_if_git_installed():
        errors.no_git_installed()
    if not utils.check_internet():
        errors.no_internet_connection()


@click.command()
@click.option("--username",
              prompt="GitHub username",
              help="Target profile username")
@click.option("--languages",
              prompt="Languages",
              default="all",
              help="Languages to be fetched")
@click.option("--create-tree",
              prompt="Arrange?",
              default=False,
              help="Whether to make the directories for arrangements or not")
def main(username, languages, create_tree):
    setup()
    languages = languages.lower()
    if languages == "all":
        git.fetch_all_repos(username)
    else:
        git.fetch_by_languages("yogesh-aggarwal",
                               languages.split(","),
                               plain_tree=not create_tree)


if __name__ == "__main__":
    main()
