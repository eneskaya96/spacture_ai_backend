import json
import requests


def add_face_detection(company_id, image_url):
    url = "http://192.168.1.34:5000/api/face_detection"
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
    url = "http://192.168.1.34:5000/api/face_detection_notify"
    data = {
        "face_detection_id": face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()


def get_all_face_detection(company_id):
    url = f"http://192.168.1.34:5000/api/face_detection/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
image_url = "8_pair"
add_face_detection(company_id, image_url)

"""

#notify_face_detected("99758de4-b84c-4bb7-b940-c674d14550d1")


company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
get_all_face_detection(company_id)