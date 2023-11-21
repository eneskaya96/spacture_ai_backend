from src.services.notificationService import NotificationService


class DetectedFaceService:

    def __init__(self, socketio):
        self.image_dir = "./src/assets"
        self.socketio = socketio

    def get_images_directory(self):
        return self.image_dir

    def notify_detected_face(self, detected_person):

        self.socketio.emit('new_detection', {'data': [detected_person]}, namespace='/')

        print("Notify is sent")

        if detected_person["thread"]:
            notification_service = NotificationService()
            notification_service.send_notification()
            print("Notification send to mobile app")
