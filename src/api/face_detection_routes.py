
from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.face_detection.notify_face_detection_request_dto import NotifyFaceDetectionRequestDto
from src.services.face_detection_service import FaceDetectionService

def initialize_face_detection_routes(app, socketio):

    @app.route('/api/face_detection', methods=['POST'])
    def face_detection_notify():
        face_detection_request_dto: NotifyFaceDetectionRequestDto = NotifyFaceDetectionRequestDto.parse_obj(
            request.get_json()
        )
        face_detection_service = FaceDetectionService(socketio)

        face_detection_service.notify_face_detected(face_detection_request_dto.face_detection_id)
        return BaseResponse.create_response(message='Face detection Notify is sent.')

