import os

from github import Github

import config
from branch_protection import create_branch_protection, check_branch_protection
from vulnerability_alerts import get_vulnerability_alerts


def main():
    repo_path = f"{config.REPO_OWNER}/{config.REPO_NAME}"

    github = Github(os.getenv('GITHUB_TOKEN'))
    repo = github.get_repo(repo_path)
    branch = repo.get_branch(config.BRANCH_NAME)

    check_branch_protection(branch, create_branch_protection)
    get_vulnerability_alerts()
    github.close()


if __name__ == "__main__":
    main()
