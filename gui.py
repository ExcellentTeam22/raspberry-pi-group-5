from flask import Flask, Response, render_template, request

import bench_dip_module
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
    return render_template("push_up.html")


@app.route('/bench_dips', methods=['POST'])
def bench_dips():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return render_template("bench_dips.html")


@app.route('/squat', methods=['POST'])
def squat():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return "squat"


def gen(module):
    while True:
        frame = module.start_exercise(0, 0)
        if frame is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/push_up_feed')
def push_up_feed():
    push_up_mod = push_up_module.PushUp()
    return Response(gen(push_up_mod),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/bench_dips_feed')
def bench_dips_feed():
    bench_dips_mod = bench_dip_module.benchDips()
    return Response(gen(bench_dips_mod),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
