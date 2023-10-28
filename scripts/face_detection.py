import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Videoyu yakala
video = cv2.VideoCapture('../assets/sample_video_1.mp4')  # Buraya videonuzun yolunu yazın.

# Kaydedilen yüzler için bir klasör oluşturun.
faces_folder = "detected_faces"
if not os.path.exists(faces_folder):
    os.makedirs(faces_folder)

# Yüzlerin ekran görüntülerini almak ve kaydetmek için bir sayaç tanımlayın.
counter = 0

while True:
    # Videoyu kare kare yakala
    ret, frame = video.read()

    # Eğer video sona erdiyse döngüden çık
    if not ret:
        break

    # Griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Yüzler için dikdörtgen çiz ve ekran görüntüsünü kaydet.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Yüzün ekran görüntüsünü al
        roi_color = frame[y:y + h, x:x + w]

        # Ekran görüntüsünü bir dosyaya kaydet
        face_filename = os.path.join(faces_folder, f"face_{counter}.png")
        cv2.imwrite(face_filename, roi_color)

        # Sayaçı güncelle
        counter += 1

    # Çerçeveyi göster
    cv2.imshow('Video', frame)

    # 'q' tuşuna basarak çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şey bittiğinde yakalamayı bırak
video.release()
cv2.destroyAllWindows()