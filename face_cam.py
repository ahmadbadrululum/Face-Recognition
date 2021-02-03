import cv2

# Load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Mengambil video camera
cap = cv2.VideoCapture(0)
# menyimpan video
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # membaca frame nya
    _, img = cap.read()

    # diconvert di grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Menggambar persegi panjang disisi wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Menampilkan camera dan wajah
    cv2.imshow('img', img)

    # esc untuk mematikan
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Menampilkan video dengan gambar dan deteksi
cap.release()
