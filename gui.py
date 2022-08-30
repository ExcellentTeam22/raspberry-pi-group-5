from flask import Flask, Response, render_template, request

from exercises import push_up_module, bench_dip_module, squat_module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/push_up', methods=['POST'])
def push_up():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return render_template("exercise.html", address="push_up_feed")


@app.route('/bench_dips', methods=['POST'])
def bench_dips():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return render_template("exercise.html", address="bench_dips_feed")


@app.route('/squat', methods=['POST'])
def squat():
    data = request.form
    sets = int(data["sets"])
    repeats = int(data["repeats"])
    return render_template("exercise.html", address="squat_feed")


def gen(module):
    while True:
        frame = module.start_exercise()
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


@app.route('/squat_feed')
def squat_feed():
    squat_mod = squat_module.squat()
    return Response(gen(squat_mod),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)
