import json
import requests
import os
from dotenv import load_dotenv

load_dotenv("../envs/local.env")

base_url = f"http://{os.getenv('IP')}:5000"


def add_shoplifting(company_id, face_detection_id, video_url):
    url = f"{base_url}/api/shoplifting_detected"
    data = {
        "company_id": company_id,
        "face_detection_id": face_detection_id,
        "video_url": video_url
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def get_shoplifting(face_detection_id):
    url = f"{base_url}/api/shoplifting/{face_detection_id}"

    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def get_all_shoplifting(company_id):
    url = f"{base_url}/api/all_shoplifting/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

"""
company_id = "7375b410-20ff-489c-95df-c198bbc32dda"
face_detection_id = "95bef5ac-d141-4be7-9c7b-362a554889a4"
video_url = "10.gif"
add_shoplifting(company_id, face_detection_id, video_url)
"""

"""
face_detection_id = "95bef5ac-d141-4be7-9c7b-362a554889a4"
get_shoplifting(face_detection_id)
"""

company_id = "7375b410-20ff-489c-95df-c198bbc32dda"
get_all_shoplifting(company_id)