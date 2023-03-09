import cv2
import requests
import numpy as np

cap = cv2.VideoCapture('face-demographics-walking-and-pause.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()
        url = 'http://localhost:3000/upload'
        files = {'image': ('myimage.jpg', img_bytes, 'image/jpeg')}
        response = requests.post(url, files=files)

    else:
        break

cap.release()
cv2.destroyAllWindows()