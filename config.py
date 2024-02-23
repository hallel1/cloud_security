REPO_OWNER = "hallel1"
REPO_NAME = "SimpleApi"
BRANCH_NAME = "master"

PASSWORD_REGEX = ("^(?=.*[0-9])" #  must contain at least one digit
                  "(?=.*[a-z])" #  must contain a single lowercase letter
                  "(?=.*[A-Z])" #  must contain a single uppercase letter
                  "(?=.*)"#  must contain one special character.
                  ".{8,16}$")# must be 8-16 characters

QUERY_URL = 'https://api.github.com/graphql'
VULNERABILITY_ALERTS_QUERY = """
    {
      repository(owner: \"""" + REPO_OWNER + """\", name: \"""" + REPO_NAME + """\") {
        vulnerabilityAlerts(first: 10) {
          edges {
        node {
          securityAdvisory {
            description
            severity
            summary
          }
          securityVulnerability {
            package {
              name
            }
            firstPatchedVersion {
              identifier
            }
     vulnerableVersionRange

            }}
          }
        }
      }
    }
    """
