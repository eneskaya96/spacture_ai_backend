from services.detected_person_service import DetectedPersonService
from services.notificationService import NotificationService


class DetectedImagesService:
    detected_person_service = DetectedPersonService()

    def __init__(self, socketio):
        self.image_dir = "./assets"
        self.detection_count = 8
        self.socketio = socketio

    def list_detected_images(cls):
        return cls.detected_person_service.get_detected_persons()

    def get_images_directory(self):
        return self.image_dir

    def send_detected_images(self, thread):
        detected_person = self.detected_person_service.create_detected_person(self.detection_count, thread)

        self.socketio.emit('new_detection', {'data': [detected_person] }, namespace='/')

        self.detection_count = 8 if self.detection_count == 12 else self.detection_count + 1

        if detected_person["thread"]:
            notification_service = NotificationService()
            notification_service.send_notification()
