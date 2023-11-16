import logging
from typing import Optional

from src.domain.face_detection.entities.face_detection import FaceDetection
from src.domain.seed_work.repository.unit_of_work import UnitOfWork
from src.services.base.base_service import BaseService
from src.services.detected_person_service import DetectedPersonService


class FaceDetectionService(BaseService):
    logger = logging.getLogger(__name__)
    detected_person_service = DetectedPersonService()

    def __init__(self, socketio, uow: Optional[UnitOfWork] = None) -> None:
        self.socketio = socketio
        super().__init__(uow)

    def notify_face_detected(self, face_detection_id: str) -> FaceDetection:
        """
        Notify face detected
        :param face_detection_id
        """

        with self.uow:
            face_detection = self.uow.face_detection.get(face_detection_id)

        self.logger.info(f'Face detection is obtained by id: {face_detection_id} ')

        detected_person = self.detected_person_service.create_detected_person(8, True)

        self.socketio.emit('new_detection', {'data': [detected_person]}, namespace='/')

        print("Notify is sent")

        return face_detection
