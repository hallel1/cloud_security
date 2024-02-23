REPO_OWNER = "hallel1"
REPO_NAME = "SimpleApi"
BRANCH_NAME = "master"

QUERY_URL = 'https://api.github.com/graphql'
VULNERABILITY_ALERTS_QUERY = """
    {
      repository(owner: \""""+REPO_OWNER+"""\", name: \""""+REPO_NAME+"""\") {
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
