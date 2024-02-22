from github import Github
import github_config
from github.Branch import Branch


def main():
    repo_name ="hallel1/learn-kafka"
    branch_name = "main"

    g = Github(github_config.GITHUB_TOKEN)
    repo = g.get_repo(repo_name)
    branch = repo.get_branch(branch_name)

    branch_protection(branch)


def branch_protection(branch: Branch) -> None:
    branch.edit_protection(
        enforce_admins=True,
        strict=True,
        contexts=[],
        required_approving_review_count=1
    )


if __name__ == "__main__":
    main()
