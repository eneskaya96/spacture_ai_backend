import uuid
import random
from datetime import datetime


class DetectedPersonService:
    detected_count = 100000
    def __init__(self, ):
        print("DetectedPersonService")
        self.detected_persons = []
        self.names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']

    def create_detected_person(self, url):
        """
        for detected_person in self.detected_persons:
            if url == detected_person["url"]:
                return detected_person
        """

        now = datetime.now()
        name = random.choice(self.names)
        thread = random.choice([ False, True])

        detected_person = {
            "id": "ID_" + str(DetectedPersonService.detected_count),
            "url": url,
            "name": name,
            "detection_date": now.strftime("%Y-%m-%d %H:%M:%S"),
            "thread": thread
        }
        print("person ", detected_person)
        DetectedPersonService.detected_count += 1
        self.detected_persons.append(detected_person)
        return detected_person

    def get_detected_persons(self):
        return self.detected_persons