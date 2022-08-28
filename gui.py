from flask import Flask, Response
import cv2
import push_up

app = Flask(__name__)


@app.route('/')
def index():
    return "Default Message"


def gen():
    exercise = push_up.PushUp()
    while True:

        frame = exercise.push_ups()
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
