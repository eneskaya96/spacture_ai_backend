

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv("../envs/local.env")

base_url = f"http://{os.getenv('IP')}:5000"


def save_token(company_id):
    url = f"{base_url}/api/save-token"
    data = {
        "company_id": company_id,
        "token": "token_2",
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def send_notification(company_id):
    url = f"{base_url}/api/send-notification/{company_id}"

    response = requests.post(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())

company = "7375b410-20ff-489c-95df-c198bbc32dda"
#save_token(company)

send_notification(company_id=company)