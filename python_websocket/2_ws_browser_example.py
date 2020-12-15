#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import json
from datetime import datetime


DT = {}
now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
DT['now'] = now


async def time(websocket, path):
    while True:
        await websocket.send(json.dumps(DT))
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
