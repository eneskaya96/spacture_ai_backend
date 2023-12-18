from flask import request

from src.api.models.base_response import BaseResponse
from src.api.models.dto.notification.notification_response_dto import NotificationResponseDto
from src.api.models.dto.notification.save_token_request_dto import SaveTokenRequestDto
from src.services.notificationService import NotificationService


def initialize_notification_routes(app):

        @app.route('/api/save-token', methods=['POST'])
        def save_token():
            save_token_request_dto: SaveTokenRequestDto = SaveTokenRequestDto.parse_obj(
                request.get_json()
            )

            notification_service = NotificationService()
            notification_token = notification_service.save_token(save_token_request_dto)
            if notification_token:
                notification_response_dto = NotificationResponseDto.create(notification_token)
                return BaseResponse.create_response(message='Notification token is created',
                                                    data=notification_response_dto)
            else:
                return BaseResponse.create_response(message='Notification token already exist')

        @app.route('/api/send-notification/<string:company_id>', methods=['POST'])
        def send_notification(company_id: str):
            notification_service = NotificationService()
            is_sent = notification_service.send_notification(company_id)

            if is_sent:
                return BaseResponse.create_response(message='Notification successfully sent')
            else:
                return BaseResponse.create_response(message='Notification is not sent')
