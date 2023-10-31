from src.services.videoStreamService import VideoStreamService


def initialize_camera_stream_routes(socketio):

    @socketio.on('start_stream_1')
    def start_stream(data):
        session_id = data.get('session_id')
        video_stream_service = VideoStreamService(socketio, './src/assets/sample_video_1.mp4', "video_frame_1")
        video_stream_service.start_stream(session_id)

    @socketio.on('start_stream_2')
    def start_stream(data):
        session_id = data.get('session_id')
        video_stream_service = VideoStreamService(socketio, './src/assets/sample_video_2.mp4', "video_frame_2")
        video_stream_service.start_stream(session_id)

    @socketio.on('start_stream_3')
    def start_stream(data):
        session_id = data.get('session_id')
        video_stream_service = VideoStreamService(socketio, './src/assets/sample_video_3.mp4', "video_frame_3")
        video_stream_service.start_stream(session_id)

    @socketio.on('start_stream_4')
    def start_stream(data):
        session_id = data.get('session_id')
        video_stream_service = VideoStreamService(socketio, './src/assets/sample_video_4.mp4', "video_frame_4")
        video_stream_service.start_stream(session_id)
