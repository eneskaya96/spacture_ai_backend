import json
import requests
import os
from dotenv import load_dotenv

load_dotenv("../envs/local.env")

base_url = f"http://{os.getenv('IP')}:5000"


def add_watchlist(company_id, face_detection_id):
    url = f"{base_url}/api/watchlist"
    data = {
        "company_id": company_id,
        "face_detection_id": face_detection_id
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def create_watchlist_face_detection(company_id, old_face_detection_id, face_detection_id):
    url = f"{base_url}/api/watchlist_face_detection"
    data = {
        "company_id": company_id,
        "old_face_detection_id": old_face_detection_id,
        "face_detection_id": face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def watchlist_detected(watchlist_face_detection_id):
    url = f"{base_url}/api/watchlist_detected"
    data = {
        "watchlist_face_detection_id": watchlist_face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def get_all_watchlist(company_id):
    url = f"{base_url}/api/watchlist/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def get_all_watchlist_face_detection(company_id):
    url = f"{base_url}/api/watchlist_face_detection/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
face_detection_id = "99758de4-b84c-4bb7-b940-c674d14550d1"
add_watchlist(company_id, face_detection_id)
"""


company_id = "7375b410-20ff-489c-95df-c198bbc32dda"
old_face_detection_id = "5d91e964-ceaa-4874-a600-baba7e67b2bf"
face_detection_id = "95bef5ac-d141-4be7-9c7b-362a554889a4"
create_watchlist_face_detection(company_id, old_face_detection_id, face_detection_id)


"""
watchlist_face_detection_id = "32ca5fca-0167-4a9c-abd9-cb510567c02d"
watchlist_detected(watchlist_face_detection_id)
"""

"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
get_all_watchlist(company_id)
"""

"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
get_all_watchlist_face_detection(company_id)
"""