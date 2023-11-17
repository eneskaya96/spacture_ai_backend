
from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.face_detection.face_detection_request_dto import FaceDetectionRequestDto
from src.api.models.dto.face_detection.face_detection_response_dto import FaceDetectionResponseDto

from src.api.models.dto.face_detection.face_detections_response_dto import FaceDetectionsResponseDto
from src.api.models.dto.face_detection.notify_face_detection_request_dto import NotifyFaceDetectionRequestDto
from src.services.face_detection_service import FaceDetectionService

def initialize_face_detection_routes(app, socketio):

    @app.route('/api/face_detection_notify', methods=['POST'])
    def face_detection_notify():
        face_detection_request_dto: NotifyFaceDetectionRequestDto = NotifyFaceDetectionRequestDto.parse_obj(
            request.get_json()
        )
        face_detection_service = FaceDetectionService(socketio)

        face_detection_service.notify_face_detected(face_detection_request_dto.face_detection_id)
        return BaseResponse.create_response(message='Face detection Notify is sent.')

    @app.route('/api/face_detection', methods=['POST'])
    def create_face_detection():
        face_detection_request_dto: FaceDetectionRequestDto = FaceDetectionRequestDto.parse_obj(
            request.get_json()
        )
        face_detection_service = FaceDetectionService(socketio)

        face_detection = face_detection_service.create_face_detection(face_detection_request_dto)
        face_detection_response_dto = FaceDetectionResponseDto.create(face_detection)
        return BaseResponse.create_response(message='Face detection created', data=face_detection_response_dto)

    @app.route('/api/face_detection/<string:company_id>', methods=['GET'])
    def get_all_face_detection(company_id: str):

        face_detection_service = FaceDetectionService(socketio)

        face_detections = face_detection_service.get_face_detections(company_id)
        face_detection_response_dto = FaceDetectionsResponseDto.create(face_detections)
        return BaseResponse.create_response(message='Face detections are get', data=face_detection_response_dto)
