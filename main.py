import json
import os

import requests
from github import Github
from github.Branch import Branch

import config


def main():
    repo_path = f"{config.REPO_OWNER}/{config.REPO_NAME}"

    github = Github(os.getenv('GITHUB_TOKEN'))
    repo = github.get_repo(repo_path)
    branch = repo.get_branch(config.BRANCH_NAME)

    check_branch_protection(branch, create_branch_protection)
    get_vulnerability_alerts()
    github.close()


def check_branch_protection(branch: Branch, create_branch_protection):
    try:
        protection = branch.get_protection()
        print_branch_protection_status(protection)
    except Exception as e:
        if e.status == 404:
            create_branch_protection(branch)
            protection = branch.get_protection()
            print_branch_protection_status(protection)
        else:
            raise e


def print_branch_protection_status(protection):
    print("Branch protection settings:")
    print(f"Required status checks: {protection.required_status_checks}")
    print(f"Enforce admins: {protection.enforce_admins}")
    print(f"Required pull request reviews: {protection.required_pull_request_reviews}\n\n")


def create_branch_protection(branch: Branch) -> None:
    print("Creating branch protection\n")
    branch.edit_protection(
        enforce_admins=True,
        strict=True,
        contexts=[],
        required_approving_review_count=1
    )


def get_vulnerability_alerts():
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}

    response = requests.post(config.QUERY_URL, json={'query': config.VULNERABILITY_ALERTS_QUERY}, headers=headers)
    if response.status_code == 200:
        alerts = extracts_alerts(response)

        print("Vulnerability alerts:")
        for alert in alerts:
            prints_vulnerability_alert(alert)
    else:
        print(f"Query failed to run by returning code of {response.status_code}\n")


def extracts_alerts(response):
    result = response.json()
    alerts = result["data"]["repository"]["vulnerabilityAlerts"]["edges"]
    return alerts


def prints_vulnerability_alert(alert):
    print(json.dumps(alert["node"], indent=4))
    print()


if __name__ == "__main__":
    main()
