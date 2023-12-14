from flask import jsonify, request
from onesignal_sdk.client import Client

from src.configs.config_manager import ConfigManager
from src.services.notificationService import NotificationService


def initialize_notification_routes(app):

        @app.route('/api/save-token', methods=['POST'])
        def save_token():
            data = request.get_json()
            if not data or 'token' not in data:
                return jsonify({'error': 'Token is missing'}), 400

            token = data['token']

            notification_service = NotificationService()
            message, response_code = notification_service.addToken(token)
            return jsonify({'message': message}), response_code

        @app.route('/api/send-notification', methods=['POST'])
        def send_notification():
            data = request.get_json()
            if data is None:
                return jsonify({'error': 'Token is missing'}), 400
            title = "SUSPICIOUS ALERT"
            message = "Suspicious behaviour detected"
            token = data['token']
            post_body = {
                "headings": {"en": title},
                "contents": {"en": message},
                "include_player_ids": [token],
            }
            config = ConfigManager.config
            one_signal_client = Client(user_auth_key=config.ONESIGNAL_USER_AUTH_KEY,
                                       rest_api_key=config.ONESIGNAL_REST_API_KEY,
                                       app_id=config.ONESIGNAL_APP_ID)
            response = one_signal_client.send_notification(post_body)
            return jsonify({'message': response.body}), response.status_code
