import requests
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
auth_url = "https://www.strava.com/oauth/token"

def auth_strava():
    payload = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'refresh_token': os.getenv('REFRESH_TOKEN'),
        'grant_type': "refresh_token",
        'f': 'json'
    }
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    return access_token