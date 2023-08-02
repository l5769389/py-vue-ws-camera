import asyncio
import time

import websocket
import websockets
from websockets.legacy.server import WebSocketServerProtocol

from config import ip, ws_port


class VideoWs:
    ws = None
    queue = None
    @staticmethod
    async def start(args, event,queue):
        VideoWs.queue = queue
        print('ws start')
        async with websockets.serve(VideoWs.ws_handle,ip ,ws_port):
            await asyncio.Future()  # run forever

    @staticmethod
    async def ws_handle(websocket: WebSocketServerProtocol, path: str):
        asyncio.create_task(VideoWs.sendMsg(websocket))
        while True:
            async for message in websocket:
                msg = await websocket.recv()
                print(msg)

    @staticmethod
    async def sendMsg(websocket):
        while True:
            msg =VideoWs.queue.get()
            await websocket.send(msg)
            await asyncio.sleep(0.001)

