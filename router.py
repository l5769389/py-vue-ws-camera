import threading
from flask import Flask, jsonify, Response
import asyncio
from camera import Camera
from websocketServer import VideoWs
from flask_cors import CORS
from config import ip, http_port
from queue import Queue

app = Flask(__name__)
CORS(app)
camera = Camera()
event = threading.Event()

queue = Queue()


@app.route('/open')
def open_camera():
    open_ws_conn()
    dic = {
        'code': 1,
        'msg': 'open camera success'
    }
    return jsonify(dic)


@app.route('/close')
def close_camera():
    camera.close_camera()
    return jsonify({
        'code': 1
    })


def open_ws_conn():
    openWs()


def run():
    print('执行')
    app.run(host=ip, port=http_port)


def main():
    flask_thread = threading.Thread(target=run, name='flask thread')
    flask_thread.start()


def openWs():
    t = threading.Thread(target=openws1, name='ws thread', args=(1, event, queue))
    t1 = threading.Thread(target=openVideo1, name='video thread', args=(1, event, queue))
    t.start()
    t1.start()


def openws1(args, event, queue):
    openws2(args, event, queue).send(None)


def openws2(args, event, queue):
    asyncio.run(VideoWs.start(args, event, queue))


def openVideo1(args, event, queue):
    openVideo(args, event, queue).send(None)


def openVideo(args, event, queue):
    asyncio.run(camera.open_camera(args, event, queue))

if __name__ == '__main__':
    main()
