

import json

import requests


def create_company():
    url = "http://192.168.1.34:5000/api/company"
    data = {
        "name": "Enes",
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())

def get_company_by_id(company_id):
    url = f"http://192.168.1.34:5000/api/company/{company_id}"
    response = requests.get(url,  headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())

create_company()
get_company_by_id("d4261a87-9367-459a-be4c-f18d82346b35")