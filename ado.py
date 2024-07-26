import sys
import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic syu4bvgl6rzsawz4umkh2qy4ihzurxca6wiuh6l4pwsjfd2z5flq",
}

# payload={
#   "name": "FabrikamTravel",
#   "description": "Frabrikam travel app for Windows Phone",
#   "capabilities": {
#     "versioncontrol": {
#       "sourceControlType": "Git"
#     },
#     "processTemplate": {
#       "templateTypeId": "6b724908-ef14-45cf-84f8-768b5384da45"
#     }
#   }
# }

response = requests.get("https://dev.azure.com/mrpl2720314/_apis/projects?api-version=7.0", headers=headers)

print(response.status_code)
print(response.text)
