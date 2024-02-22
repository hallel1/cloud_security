from github import Github
from github.Branch import Branch
import os


def main():
    repo_name = "hallel1/learn-kafka"
    branch_name = "main"

    github = Github(os.getenv('GITHUB_TOKEN'))
    repo = github.get_repo(repo_name)
    branch = repo.get_branch(branch_name)

    check_branch_protection(branch, create_branch_protection)


def check_branch_protection(branch: Branch, create_branch_protection):
    try:
        protection = branch.get_protection()
        print("Branch protection settings:")
        print(f"Required status checks: {protection.required_status_checks}")
        print(f"Enforce admins: {protection.enforce_admins}")
        print(f"Required pull request reviews: {protection.required_pull_request_reviews}")
    except Exception as e:
        if e.status == 404:
            create_branch_protection(branch)
        else:
            raise e


def create_branch_protection(branch: Branch) -> None:
    print("Creating branch protection")
    branch.edit_protection(
        enforce_admins=True,
        strict=True,
        contexts=[],
        required_approving_review_count=1
    )


if __name__ == "__main__":
    main()
