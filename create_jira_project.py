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

    with open('payload.json') as f:
        payload = json.load(f)

    response = requests.post(
       url,
       json=payload,
       headers=headers,
       auth=auth
    )

    print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth)

    response_data = json.loads(response.text)
    print(json.dumps(response_data, sort_keys=True, indent=4, separators=(",", ": ")))

    if response.status_code != 201 or response_data.get('errors'):
        sys.exit(1)

if __name__ == "__main__":
    main()
