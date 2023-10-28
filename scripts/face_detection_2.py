import dlib
import cv2

# Dlib'in yüz dedektörünü yükle
detector = dlib.get_frontal_face_detector()

# Video yakalama
video = cv2.VideoCapture('../assets/sample_video_1.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Dlib ile yüz tespiti yap
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x, y = face.left(), face.top()
        w, h = face.right() - x, face.bottom() - y

        # yüz etrafında bir dikdörtgen çiz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
