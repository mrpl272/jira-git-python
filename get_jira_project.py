import os
import requests
from requests.auth import HTTPBasicAuth
import json

def main():
    url = "https://mrpl272.atlassian.net/rest/api/3/project"

    auth = HTTPBasicAuth(os.getenv("JIRA_USER"), os.getenv("JIRA_API_TOKEN"))

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    response = requests.get(
       url,
       headers=headers,
       auth=auth
    )

    # print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))

    with open('projects.json', 'w') as f:
        json.dump(response.json(), f, sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == "__main__":
    main()
