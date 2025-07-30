# 👨‍🏫 Face Recognition Attendance System using OpenCV and Face_Recognition

A real-time attendance system that uses face recognition to mark attendance automatically using a webcam. Built with Python, OpenCV, and the `face_recognition` library.

---

## 📁 Project Structure

```
FaceAttendanceProject/
│
├── known_faces/                 # Folder containing images of known persons
│   └── (e.g., Alice.jpg, Bob.jpg)
│
├── images/                      # (Optional) Original raw images
│
├── encodings.pickle            # Precomputed facial encodings (generated)
│
├── Attendance.csv              # Attendance log file (auto-created or updated)
│
├── main.py                     # Main script to start webcam and mark attendance
│
├── utils.py                    # Helper function to log attendance
│
├── encode_faces.py             # Script to generate encodings from known_faces/
│
└── README.md                   # Project documentation
```

---

## ⚙️ Requirements

Install the required packages before running the code:

```bash
pip install opencv-python face_recognition numpy
```

> **Note**: The `face_recognition` package may require `cmake`, `dlib`, and build tools depending on your OS.

---

## 🚀 How to Run

### 1. Add known faces
Place images of people (e.g., `Ayushman Kar.jpg`) inside the `known_faces/` folder. The image filename (without extension) will be used as the person's name.

---

### 2. Generate encodings

```bash
python encode_faces.py
```

This will create an `encodings.pickle` file that stores facial embeddings for all images in `known_faces/`.

---

### 3. Start the attendance system

```bash
python main.py
```

- A webcam window will open.
- When a known face is detected, the name is displayed, and the person's attendance is recorded in `Attendance.csv`.

Press `q` to exit the webcam window.

---

## 🧠 How It Works

- Face encodings are computed from `known_faces/`.
- Webcam frames are captured in real-time and resized for faster recognition.
- Detected faces are compared with known encodings.
- If a match is found, the name is displayed and marked in `Attendance.csv` with the current date and time.

---

## 📝 CSV Format (Attendance.csv)

```
Name, Date, Time
Ayushman Kar, 2025-07-29, 10:35:12
Kohlii, 2025-07-29, 10:36:05
```

---

## 🛠 Troubleshooting

- **PermissionError on `attendance.csv`**: Make sure the file isn't opened in Excel or another app when running `main.py`.
- **Face not detected?** Make sure:
  - The webcam has enough light.
  - The person’s face is clearly visible and matches the image in `known_faces/`.

---

## 📌 Credits

- Built with: [`face_recognition`](https://github.com/ageitgey/face_recognition)
- Developed by: [Ayushman Kar](https://github.com/Ayushmankar14)

---

## 🌐 GitHub

View the source code here:  
🔗 [GitHub Repo](https://github.com/Ayushmankar14/ComputerVisionProject2.git)