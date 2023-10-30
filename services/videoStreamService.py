import base64
from time import sleep

import cv2

from services.detected_images import DetectedImagesService


class VideoStreamService:
    active_streams = set()

    def __init__(self, socketio, video_url, video_frame):
        self.video_url = video_url
        self.video_frame = video_frame
        self.socketio = socketio
        self.detected_images_service = DetectedImagesService(self.socketio)

    def gen_camera(self, session_id):
        cap = cv2.VideoCapture(self.video_url)
        if not cap.isOpened():
            print("Error: Couldn't open the video file.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = 1 / fps
        elapsed_time = 0
        notification_sent = False
        notification_2_sent = False
        notification_3_sent = False
        notification_4_sent = False
        notification_5_sent = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            #send notification only from only 1 camera
            if 5 <= elapsed_time <= 6 and not notification_sent and session_id == "unique_id_for_client_1" :
                notification_sent = True
                self.detected_images_service.send_detected_images(False)

            if 6 <= elapsed_time <= 7 and not notification_2_sent and session_id == "unique_id_for_client_1":
                notification_2_sent = True
                self.detected_images_service.send_detected_images(False)

            if 10 <= elapsed_time <= 11 and not notification_3_sent and session_id == "unique_id_for_client_1":
                notification_3_sent = True
                self.detected_images_service.send_detected_images(False)
            if 11 < elapsed_time <= 12 and not notification_4_sent and session_id == "unique_id_for_client_1":
                notification_4_sent = True
                self.detected_images_service.send_detected_images(True)


            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')

            # Use socketio.emit instead of the simple emit
            self.socketio.emit(self.video_frame, {'image': 'data:image/jpeg;base64,' + jpg_as_text}, namespace='/')

            self.socketio.sleep(delay)
            elapsed_time += delay

        if session_id == "unique_id_for_client_1":
            self.detected_images_service.send_detected_images(False)
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

    def restart_stream(self, session_id):
        print("restart_stream")

