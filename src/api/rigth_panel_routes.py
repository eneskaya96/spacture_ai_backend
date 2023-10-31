from flask import send_from_directory, jsonify

from src.services.detected_images import DetectedImagesService


def initialize_right_panel_routes(app, socketio):

    @app.route('/list_detected_images', methods=['GET'])
    def list_detected_images():
        detected_images_service = DetectedImagesService(socketio)
        images = detected_images_service.list_detected_images()

        return jsonify(images)

    @app.route('/image/<filename>')
    def serve_image(filename):
        detected_images_service = DetectedImagesService(socketio)
        return send_from_directory(detected_images_service.get_images_directory(), filename)
