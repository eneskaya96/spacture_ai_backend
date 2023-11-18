
from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.watchlist.watchlist_detected_request_dto import WatchlistDetectedRequestDto
from src.api.models.dto.watchlist.watchlist_face_detection_request_dto import WatchlistFaceDetectionRequestDto
from src.api.models.dto.watchlist.watchlist_face_detection_response_dto import WatchlistFaceDetectionResponseDto
from src.api.models.dto.watchlist.watchlist_request_dto import WatchlistRequestDto
from src.api.models.dto.watchlist.watchlist_response_dto import WatchlistResponseDto
from src.api.models.dto.watchlist.watchlists_response_dto import WatchlistsResponseDto
from src.services.watchlist_service import WatchlistService


def initialize_watchlist_routes(app, socketio):

    @app.route('/api/watchlist', methods=['POST'])
    def create_watchlist():
        watchlist_request_dto: WatchlistRequestDto = WatchlistRequestDto.parse_obj(
            request.get_json()
        )
        watchlist_service = WatchlistService(socketio)

        watchlist = watchlist_service.create_watchlist(watchlist_request_dto)
        watchlist_response_dto = WatchlistResponseDto.create(watchlist)
        return BaseResponse.create_response(message='Watchlist is created', data=watchlist_response_dto)

    @app.route('/api/watchlist/<string:company_id>', methods=['GET'])
    def get_all_watchlist(company_id: str):
        watchlist_service = WatchlistService(socketio)

        watchlists = watchlist_service.get_face_detections(company_id)
        print("watchlists", watchlists)
        watchlists_response_dto = WatchlistsResponseDto.create(watchlists)
        return BaseResponse.create_response(message='Watchlists are get', data=watchlists_response_dto)

    @app.route('/api/watchlist_face_detection', methods=['POST'])
    def create_watchlist_face_detection():
        watchlist_face_detection_request_dto: WatchlistFaceDetectionRequestDto = WatchlistFaceDetectionRequestDto.parse_obj(
            request.get_json()
        )
        watchlist_service = WatchlistService(socketio)

        watchlist_face_detection = watchlist_service.create_watchlist_face_detection(
            watchlist_face_detection_request_dto)
        watchlist_face_detection_response_dto = WatchlistFaceDetectionResponseDto.create(watchlist_face_detection)
        return BaseResponse.create_response(message='Watchlist Face detection is created',
                                            data=watchlist_face_detection_response_dto)

    @app.route('/api/watchlist/<string:company_id>', methods=['GET'])
    def get_all_watchlist_face_detection(company_id: str):
        watchlist_service = WatchlistService(socketio)

        watchlists = watchlist_service.get_face_detections(company_id)
        print("watchlists", watchlists)
        watchlists_response_dto = WatchlistsResponseDto.create(watchlists)
        return BaseResponse.create_response(message='Watchlists are get', data=watchlists_response_dto)

    @app.route('/api/watchlist_detected', methods=['POST'])
    def watchlist_detected():
        watchlist_detected_request_dto: WatchlistDetectedRequestDto = WatchlistDetectedRequestDto.parse_obj(
            request.get_json()
        )
        watchlist_service = WatchlistService(socketio)

        watchlist_service.notify_watchlist_detected(watchlist_detected_request_dto.watchlist_face_detection_id)
        return BaseResponse.create_response(message='Watchlist detected notified')

