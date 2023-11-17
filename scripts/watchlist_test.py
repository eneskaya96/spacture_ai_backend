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


def create_watchlist_face_detection(watchlist_id, face_detection_id):
    url = "http://192.168.1.34:5000/api/watchlist_face_detection"
    data = {
        "watchlist_id": watchlist_id,
        "face_detection_id": face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def watchlist_detected(watchlist_face_detection_id):
    url = "http://192.168.1.34:5000/api/watchlist_detected"
    data = {
        "watchlist_face_detection_id": watchlist_face_detection_id,
    }

    json_data = json.dumps(data)

    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

def get_all_watchlist(company_id):
    url = f"http://192.168.1.34:5000/api/watchlist/{company_id}"
    response = requests.get(url, headers={'Content-Type': 'application/json'})

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response.json()

"""
company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
face_detection_id = "99758de4-b84c-4bb7-b940-c674d14550d1"
add_watchlist(company_id, face_detection_id)
"""

"""
watchlist_id = "4b041a23-9e33-4a70-afb4-dc7cdccee59f"
face_detection_id = "684744be-6600-4162-ad7d-364c37456d5c"
create_watchlist_face_detection(watchlist_id, face_detection_id)

"""

"""
watchlist_face_detection_id = "32ca5fca-0167-4a9c-abd9-cb510567c02d"
watchlist_detected(watchlist_face_detection_id)
"""

company_id = "4d1bc09a-a089-4cd5-bc13-843345c27af3"
get_all_watchlist(company_id)