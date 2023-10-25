from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import send_from_directory
from flask_socketio import SocketIO
import gevent.monkey
gevent.monkey.patch_all(ssl=False)

from flask_apscheduler import APScheduler

from services.detected_images import DetectedImagesService
from services.notificationService import NotificationService
from services.videoStreamService import VideoStreamService

ip = "192.168.1.57"

app = Flask(__name__)
scheduler = APScheduler()
CORS(app, resources={r"*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')


"""
VIDEO STREAM 
"""
@socketio.on('start_stream_1')
def start_stream(data):
    session_id = data.get('session_id')
    video_stream_service = VideoStreamService(socketio, './assets/sample_video_2.mp4', "video_frame_1")
    video_stream_service.start_stream(session_id)


@socketio.on('start_stream_2')
def start_stream(data):
    session_id = data.get('session_id')
    video_stream_service = VideoStreamService(socketio, './assets/sample_video_3.mp4', "video_frame_2")
    video_stream_service.start_stream(session_id)

@socketio.on('start_stream_3')
def start_stream(data):
    session_id = data.get('session_id')
    video_stream_service = VideoStreamService(socketio, './assets/sample_video_old.mp4', "video_frame_3")
    video_stream_service.start_stream(session_id)

@socketio.on('start_stream_4')
def start_stream(data):
    session_id = data.get('session_id')
    video_stream_service = VideoStreamService(socketio, './assets/sample_video_2.mp4', "video_frame_4")
    video_stream_service.start_stream(session_id)



"""
RIGHT PANEL END POINTS
"""
@app.route('/list_detected_images', methods=['GET'])
def list_detected_images():
    detected_images_service = DetectedImagesService(socketio)
    images = detected_images_service.list_detected_images()

    return jsonify(images)


@app.route('/image/<filename>')
def serve_image(filename):
    detected_images_service = DetectedImagesService(socketio)
    return send_from_directory(detected_images_service.get_images_directory(), filename)


"""
NOTIFICATION END POINTS
"""
@app.route('/api/save-token', methods=['POST'])
def save_token():
    print("SAVE TOKEN")
    data = request.get_json()
    if not data or 'token' not in data:
        return jsonify({'error': 'Token is missing'}), 400

    token = data['token']

    notification_service = NotificationService()
    message, response_code = notification_service.addToken(token)
    return jsonify({'message': message}), response_code


if __name__ == '__main__':
    # flask async job
    """
    detected_images_service = DetectedImagesService(socketio)
    scheduler.add_job(id='send_new_detection_task', func=detected_images_service.send_detected_images, trigger='interval',
                      seconds=30)
    scheduler.start()
    """

    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler

    http_server = WSGIServer((ip, 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
