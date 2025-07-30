import cv2
import numpy as np
import face_recognition
import pickle
from utils import mark_attendance

# ------------ 🔐 Load encodings ------------
with open('encodings.pickle', 'rb') as f:
    data = pickle.load(f)

encodeListKnown = data['encodings']
classNames = data['names']

# ------------ 🎥 Start webcam ------------
cap = cv2.VideoCapture(0)
print("[INFO] Starting webcam...")

while True:
    success, img = cap.read()
    if not success:
        continue

    # Resize and convert for faster processing
    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Detect faces and encodings in the current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            # Scale back face location
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # Draw rectangle and name
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # ✅ Mark attendance
            mark_attendance(name)

    cv2.imshow('Face Attendance', img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
