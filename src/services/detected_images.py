import logging
from typing import Dict

from src.configs.config_manager import ConfigManager
from src.services.notificationService import NotificationService


class DetectedFaceService:
    logger = logging.getLogger(__name__)

    def __init__(self, socketio):
        self.image_dir = ConfigManager.config.IMAGE_DIR
        self.socketio = socketio

    def get_images_directory(self):
        return self.image_dir

    def notify_detected_face(self, detected_person: Dict, company_id: str, title: str = "", message: str = ""):

        self.socketio.emit('new_detection', {'data': [detected_person]}, namespace='/')

        self.logger.info(f'Notify is sent: {detected_person} ')

        if detected_person["thread"]:
            notification_service = NotificationService()
            notification_service.send_notification(company_id, title, message)
            self.logger.info(f'Notification send to mobile app: {detected_person} ')
