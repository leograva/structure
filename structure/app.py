from flask import Flask,jsonify
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route("/health/check")
def index():
    message = {'status':'UP'}
    return jsonify(message)


if __name__ == "__main__":
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()