from mtcnn import MTCNN
import cv2
import os

# MTCNN yüz dedektörünü başlat
detector = MTCNN(min_face_size=20)

# Video yakalama
video = cv2.VideoCapture('./assets/sample_video_2.mp4')

# Yüzlerin ekran görüntülerini kaydetmek için bir klasör oluşturun.
faces_folder = "detected_faces"
if not os.path.exists(faces_folder):
    os.makedirs(faces_folder)

# Yüzlerin ekran görüntülerini almak ve kaydetmek için bir sayaç tanımlayın.
counter = 0

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Görüntüden yüzleri tespit et
    faces = detector.detect_faces(frame)

    for face in faces:
        # Her yüz için bounding box koordinatlarını alın
        x, y, width, height = face['box']
        x2, y2 = x + width, y + height

        # Görüntüde yüz etrafında bir dikdörtgen çizin
        cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 2)

        # Yüzün ekran görüntüsünü al
        roi_color = frame[y:y2, x:x2]

        # Ekran görüntüsünü bir dosyaya kaydet
        face_filename = os.path.join(faces_folder, f"face_{counter}.png")
        cv2.imwrite(face_filename, roi_color)

        # Sayaçı güncelle
        counter += 1

    # Sonucu göster
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
