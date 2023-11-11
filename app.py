from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_socketio import SocketIO

import gevent.monkey

from src.configs.config_manager import ConfigManager

gevent.monkey.patch_all(ssl=False)

ip = "192.168.1.57"


if __name__ == '__main__':
    app = Flask(__name__)
    scheduler = APScheduler()
    CORS(app, resources={r"*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

    # flask async job
    """
    detected_images_service = DetectedImagesService(socketio)
    scheduler.add_job(id='send_new_detection_task', func=detected_images_service.send_detected_images, trigger='interval',
                      seconds=30)
    scheduler.start()
    """

    config = ConfigManager.init_config()
    app.config.from_object(config)

    from src.api import initialize_routes
    initialize_routes(app, socketio)

    from src.infrastructure.db.db_manager import DBManager
    DBManager.start_db(app)

    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler

    http_server = WSGIServer((ip, 5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
