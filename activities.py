from auth_strava import auth_strava
import requests
import os
import json

access_token = auth_strava()
print(access_token)

url = f"https://www.strava.com/api/v3/athlete/activities"
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(url, headers=headers)
print(response.json())