from github.Branch import Branch


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

