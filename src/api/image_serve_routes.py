from flask import send_from_directory

from src.services.detected_images import DetectedFaceService


def initialize_image_serve_routes(app, socketio):

    @app.route('/image/<filename>')
    def serve_image(filename):
        detected_face_service = DetectedFaceService(socketio)
        return send_from_directory(detected_face_service.get_images_directory(), filename)
