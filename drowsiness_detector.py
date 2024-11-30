# drowsiness_detector.py
import cv2

def detect_drowsiness(frame):
    # Load OpenCV's pre-trained eye cascade for eye detection
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    drowsy = len(eyes) == 0  # If no eyes are detected, assume drowsiness
    return drowsy, frame
