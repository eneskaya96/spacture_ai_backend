import base64
from time import sleep

import cv2

class VideoStreamService:
    active_streams = set()

    def __init__(self, socketio, video_url, video_frame):
        self.video_url = video_url
        self.video_frame = video_frame
        self.socketio = socketio

    def gen_camera(self, session_id):
        cap = cv2.VideoCapture(self.video_url)
        if not cap.isOpened():
            print("Error: Couldn't open the video file.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = 1 / fps
        elapsed_time = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Use socketio.emit instead of the simple emit
            self.socketio.emit(self.video_frame, {'image': 'data:image/jpeg;base64,' + jpg_as_text}, namespace='/')

            self.socketio.sleep(delay)
            elapsed_time += delay

        cap.release()
        sleep(1)
        """
        VideoStreamService.active_streams.remove(session_id)
        self.start_stream(session_id)
        """

    def is_stream_active(cls, session_id):
        return session_id in cls.active_streams

    def start_stream(self, session_id):
        if not self.is_stream_active(session_id):
            VideoStreamService.active_streams.add(session_id)
            self.socketio.start_background_task(target=self.gen_camera,  session_id=session_id)
