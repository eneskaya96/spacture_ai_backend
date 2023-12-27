import logging

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from src.configs.config_manager import ConfigManager


def create_app():

    import gevent.monkey
    gevent.monkey.patch_all(ssl=False)

    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

    config = ConfigManager.init_config()
    app.config.from_object(config)

    from src.infrastructure.logging.log_manager import LogManager
    LogManager.init_logger(config)

    from src.api import initialize_routes
    initialize_routes(app, socketio)

    from src.infrastructure.db.db_manager import DBManager
    DBManager.start_db(app)

    return app


logger = logging.getLogger(__name__)
logger.info(f'Spacture AI Backend is Alive')

app = create_app()