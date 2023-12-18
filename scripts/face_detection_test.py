import json
import requests
import os
from dotenv import load_dotenv

load_dotenv("../envs/local.env")

base_url = f"http://{os.getenv('IP')}:5000"

def add_face_detection(company_id, image_url):
    url = f"{base_url}/api/face_detection"
    data = {
        "company_id": company_id,
        "image_url": image_url
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def notify_face_detected(face_detection_id):
    url = f"{base_url}/api/face_detection_notify"
    data = {
        "face_detection_id": face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def get_all_face_detection(company_id):
    url = f"{base_url}/api/face_detection/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()



company_id = "7375b410-20ff-489c-95df-c198bbc32dda"
image_url = "11"
add_face_detection(company_id, image_url)
"""

notify_face_detected("49617e5c-7b65-46cf-9128-30ad4c2a3e30")

"""
"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
get_all_face_detection(company_id)
"""