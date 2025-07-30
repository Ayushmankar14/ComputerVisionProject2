import csv
from datetime import datetime
import os

def mark_attendance(name, filename=r'C:\Users\workp\PycharmProjects\FaceAttendanceProject\attendance.csv'):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Date', 'Time'])

    with open(filename, 'r+', newline='') as f:
        lines = f.readlines()
        names = [line.split(',')[0] for line in lines[1:]]  # skip header

        if name not in names:
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')
            date_str = now.strftime('%Y-%m-%d')
            f.write(f'{name},{date_str},{time_str}\n')
