import os
import json
import utils
import requests


class Repository:
    username: str | None = None
    name: str | None = None
    language: str | None = None

    def __init__(self, username: str, name: str, language: str | None = None):
        self.username = username
        self.name = name
        self.language = language

    def fetch(self):
        print(f"== FETCHING: {self.name} =====================")
        utils.run_command(
            f"git clone https://github.com/{self.username}/{self.name} --recursive"
        )
        print()


def fetch_repos(repos: list[Repository]):
    for repo in repos:
        repo.fetch()


def fetch_by_languages(username: str,
                       languages: list[str],
                       plain_tree: bool = True):
    api_response = requests.get(
        f"https://api.github.com/users/{username}/repos")
    repos: list[dict] = json.loads(api_response.text)

    # Filter repos
    repos_to_be_fetched: list[Repository] = []
    for repo in repos:
        if repo["language"] is None:
            continue
        if repo["language"].lower() in languages:
            repos_to_be_fetched.append(
                Repository(username, repo["name"], repo["language"]))

    # Fetch them one by one
    for repo in repos_to_be_fetched:
        if not plain_tree:
            os.makedirs(repo.language, exist_ok=True)
            os.chdir(repo.language)
        repo.fetch()
        if not plain_tree:
            os.chdir("../")