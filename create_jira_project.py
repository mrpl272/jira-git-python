import os
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mrpl272.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(os.getenv("JIRA_USER"), os.getenv("JIRA_API_TOKEN"))

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "assigneeType": "PROJECT_LEAD",
  "avatarId": 10200,
#   "categoryId": 10120,
  "description": "Cloud migration initiative",
#   "issueSecurityScheme": 10001,
  "key": "EX",
  "leadAccountId": "712020:d662bf67-24fd-4405-abf5-a3e80dd4be3c",
  "name": "Example",
#   "notificationScheme": 10021,
#   "permissionScheme": 10011,
  "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
  "projectTypeKey": "business",
#   "url": "http://atlassian.com"
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
