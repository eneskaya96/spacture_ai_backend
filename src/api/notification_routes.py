from flask import jsonify, request

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
