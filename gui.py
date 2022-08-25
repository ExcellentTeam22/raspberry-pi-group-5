from flask import Flask, Response
import cv2
import push_up

app = Flask(__name__)


@app.route('/')
def index():
    return "Default Message"


def gen(video):
    while True:
        frame = push_up.push_ups()
        while frame is None:
            frame = push_up.push_ups()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    global Video
    return Response(gen(push_up.push_ups()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
