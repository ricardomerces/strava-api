from auth_strava import auth_strava
import requests
import os
import json

access_token = auth_strava()
ATHLETE_ID = os.getenv('ATHLETE_ID')

url = f"https://www.strava.com/api/v3/athletes/{ATHLETE_ID}/stats"
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(url, headers=headers)
print(response.json())