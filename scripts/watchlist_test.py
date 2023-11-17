import json
import requests


def add_watchlist(company_id, face_detection_id):
    url = "http://192.168.1.34:5000/api/watchlist"
    data = {
        "company_id": company_id,
        "face_detection_id": face_detection_id
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()



company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
face_detection_id = "99758de4-b84c-4bb7-b940-c674d14550d1"
add_watchlist(company_id, face_detection_id)
