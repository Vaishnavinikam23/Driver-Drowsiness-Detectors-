# app.py
from flask import Flask, render_template, Response
from drowsiness_detector import detect_drowsiness
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # Open default camera

def gen_frames():
    while True:
        success, frame = camera.read()  # Capture frame-by-frame
        if not success:
            break
        else:
            drowsy, frame = detect_drowsiness(frame)  # Check for drowsiness
            if drowsy:
                cv2.putText(frame, "Drowsiness Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')  # Main page

@app.route('/video_feed')
def video_feed():
    # Video streaming route
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
