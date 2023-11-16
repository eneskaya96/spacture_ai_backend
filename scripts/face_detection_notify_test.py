import json
import requests


def notify_face_detected():
    url = "http://192.168.1.34:5000/api/face_detection"
    data = {
        "face_detection_id": "b0baf6ae-e74d-49b8-98b0-b3f25a22b5e7",
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

notify_face_detected()