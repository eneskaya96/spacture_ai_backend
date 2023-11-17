

def initialize_routes(app, socketio):

    from src.api.camera_stream_routes import initialize_camera_stream_routes
    initialize_camera_stream_routes(socketio=socketio)

    from src.api.notification_routes import initialize_notification_routes
    initialize_notification_routes(app=app)

    from src.api.rigth_panel_routes import initialize_right_panel_routes
    initialize_right_panel_routes(app=app, socketio=socketio)

    from src.api.company_routes import initialize_company_routes
    initialize_company_routes(app=app)

    from src.api.face_detection_routes import initialize_face_detection_routes
    initialize_face_detection_routes(app=app, socketio=socketio)

    from src.api.watchlist_routes import initialize_watchlist_routes
    initialize_watchlist_routes(app=app, socketio=socketio)
