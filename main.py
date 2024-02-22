from github import Github
from github.Branch import Branch
import os


def main():
    repo_name ="hallel1/learn-kafka"
    branch_name = "main"

    github = Github(os.getenv('GITHUB_TOKEN'))
    repo = github.get_repo(repo_name)
    branch = repo.get_branch(branch_name)

    check_branch_protection(branch, create_branch_protection)


def branch_protection(branch: Branch) -> None:
    branch.edit_protection(
        enforce_admins=True,
        strict=True,
        contexts=[],
        required_approving_review_count=1
    )


if __name__ == "__main__":
    main()
