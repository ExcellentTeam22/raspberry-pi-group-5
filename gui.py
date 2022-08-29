from flask import Flask, Response, render_template, request
import push_up_module

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/push_up', methods=['POST'])
def push_up():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return "push_up"


@app.route('/beench_dips', methods=['POST'])
def beench_dips():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return "beench_dips"


def gen():
    exercise = push_up_module.PushUp()
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
