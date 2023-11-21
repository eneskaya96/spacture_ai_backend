

import json
import os
import requests
from dotenv import load_dotenv

load_dotenv("../envs/local.env")

base_url = f"http://{os.getenv('IP')}:5000"
def create_company():
    url = f"{base_url}/api/company"
    data = {
        "name": "Enes",
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def get_company_by_id(company_id):
    url = f"{base_url}/api/company/{company_id}"
    response = requests.get(url,  headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())

#company = create_company()
#print("company_id", company['data']['id'] )
get_company_by_id("4d1bc09a-a089-4cd5-bc13-843345c27af3")