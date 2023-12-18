from http import HTTPStatus
from typing import Optional

import logging

from onesignal_sdk.client import Client

from src.api.models.dto.notification.save_token_request_dto import SaveTokenRequestDto
from src.configs.config_manager import ConfigManager
from src.domain.seed_work.repository.unit_of_work import UnitOfWork

from src.domain.notification.entities.notification import Notification
from src.services.base.base_service import BaseService


class NotificationService(BaseService):
    logger = logging.getLogger(__name__)

    def __init__(self, uow: Optional[UnitOfWork] = None) -> None:
        super().__init__(uow)

    def save_token(self, save_token_request_dto: SaveTokenRequestDto) -> Optional[Notification]:
        """
        Create a new token
        :param save_token_request_dto
        """

        notification_token = self.uow.notification.get_token(save_token_request_dto.token)
        if notification_token:
            self.logger.error(f"Token already exist in DB token: {save_token_request_dto.token}")
            return None

        new_notification_token = Notification.create_notification_token(
            company_id=save_token_request_dto.company_id,
            token=save_token_request_dto.token)

        with self.uow:
            self.uow.notification.insert(new_notification_token)

        self.logger.info(f'Notification token is created for  request: {save_token_request_dto}')

        return new_notification_token

    def send_notification(self, company_id: str) -> bool:
        config = ConfigManager.config
        if not config.ONESIGNAL_REST_API_KEY:
            self.logger.error(f"ONESIGNAL_REST_API_KEY not found")
            return False

        notification_tokens = self.uow.notification.get_tokens_by_company_id(company_id)

        if len(notification_tokens) <= 0:
            self.logger.info(f"There is no token for this company: {company_id} on DB")
            return False

        title = "SUSPICIOUS ALERT"
        message = "Suspicious behaviour detected"

        include_player_ids =[notification_token.token for notification_token in notification_tokens]
        post_body = {
            "headings": {"en": title},
            "contents": {"en": message},
            "include_player_ids": include_player_ids,
        }

        one_signal_client = Client(user_auth_key=config.ONESIGNAL_USER_AUTH_KEY,
                                   rest_api_key=config.ONESIGNAL_REST_API_KEY,
                                   app_id=config.ONESIGNAL_APP_ID)
        response = one_signal_client.send_notification(post_body)

        if not response.status_code == HTTPStatus.OK:
            self.logger.error(f"There is no error on one signal client response : {response}")
            return False

        return True
