import os
import cv2
import face_recognition
import pickle
from PIL import Image
import numpy as np

dataset_path = "known_faces"  # Make sure this folder exists and contains your images
encoding_file = "encodings.pickle"

known_encodings = []
known_names = []

print("[INFO] Loading and fixing images...")

for filename in os.listdir(dataset_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        name = os.path.splitext(filename)[0]
        path = os.path.join(dataset_path, filename)

        try:
            # Load with PIL to sanitize mode
            pil_image = Image.open(path).convert("RGB")
            print(f"[🧾] {filename}")

            # Convert to numpy array
            rgb_image = np.array(pil_image)

            # Face detection
            boxes = face_recognition.face_locations(rgb_image)
            if len(boxes) == 0:
                print(f"[❌] No face found in {filename}")
                continue

            encodings = face_recognition.face_encodings(rgb_image, boxes)
            known_encodings.extend(encodings)
            known_names.extend([name] * len(encodings))

        except Exception as e:
            print(f"[❌] Error in {filename}: {e}")

# Save encodings
print("[💾] Saving encodings...")
data = {"encodings": known_encodings, "names": known_names}

with open(encoding_file, "wb") as f:
    pickle.dump(data, f)

print("[✅] All encodings saved to encodings.pickle")
