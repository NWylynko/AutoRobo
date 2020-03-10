#!/usr/bin/env python3

# pip
from aiohttp import web
import socketio

# global
import json
import time

# local
import parser
import utils
import handler

# creates a Socket and http (thou dont need the http server) Server
sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.on('map_publish')
async def map_message(sid, message):
    data = parser.Base64MessageToDictionary(message)
    
    print(data)

    # utils.logToFile(data)

    # handler.Frame(data)

    # handler.LandMarks(data)


# run on port 3000 as the openvslam connects to a socket server on this port
web.run_app(app, port=3000)