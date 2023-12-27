from http import HTTPStatus

from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.pagination_request_dto import PaginationRequestDto
from src.api.models.dto.shoplifting.shoplifting_detected_request_dto import ShopliftingDetectedRequestDto
from src.api.models.dto.shoplifting.shoplifting_response_dto import ShopliftingResponseDto
from src.api.models.dto.shoplifting.shopliftings_response_dto import ShopliftingsResponseDto
from src.services.shoplifting_service import ShopliftingService


def initialize_shoplifting_routes(app, socketio):

    @app.route('/api/shoplifting_detected', methods=['POST'])
    def shoplifting_detected():
        shoplifting_request_dto: ShopliftingDetectedRequestDto = ShopliftingDetectedRequestDto.parse_obj(
            request.get_json()
        )
        shoplifting_service = ShopliftingService(socketio)

        shoplifting = shoplifting_service.shoplifting_detected(shoplifting_request_dto)
        shoplifting_response_dto = ShopliftingResponseDto.create(shoplifting)
        return BaseResponse.create_response(message='Shoplifting created', data=shoplifting_response_dto)

    @app.route('/api/shoplifting/<string:face_detection_id>', methods=['GET'])
    def get_shoplifting(face_detection_id: str):
        shoplifting_service = ShopliftingService(socketio)

        shoplifting = shoplifting_service.get_shoplifting(face_detection_id)
        if shoplifting:
            shoplifting_response_dto = ShopliftingResponseDto.create(shoplifting)
            return BaseResponse.create_response(message='Shoplifting is get', data=shoplifting_response_dto)
        else:
            return BaseResponse.create_response(message='Shoplifting is not Found', status_code=HTTPStatus.NO_CONTENT)

    @app.route('/api/all_shoplifting/<string:company_id>', methods=['GET'])
    def get_all_shoplifting(company_id: str):
        request_data = request.get_json(silent=True)
        default_limit = 10
        default_offset = 0

        if request_data is None:
            limit = default_limit
            offset = default_offset
        else:
            pagination_request_dto = PaginationRequestDto.parse_obj(request_data)
            limit = pagination_request_dto.limit if pagination_request_dto.limit is not None else default_limit
            offset = pagination_request_dto.offset if pagination_request_dto.offset is not None else default_offset

        shoplifting_service = ShopliftingService(socketio)

        all_shoplifting = shoplifting_service.get_all_shoplifting(company_id,
                                                                     limit,
                                                                     offset)
        face_detection_response_dto = ShopliftingsResponseDto.create(all_shoplifting)
        return BaseResponse.create_response(message='All Shoplifting are get', data=face_detection_response_dto)
