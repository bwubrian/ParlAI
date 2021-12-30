#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    ip = "73.63.216.151" # local
    #ip = "192.168.193.140" # latte
    uri = f"ws://{ip}:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
