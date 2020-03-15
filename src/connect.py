#!/usr/bin/env python3

# pip
import socketio

# global
import json
import time

# local
import parser
import utils
import handler

# creates a Socket Client
sio = socketio.Client()
sio.connect('http://localhost:3001')

@sio.on('map_publish')
def map_message(message):
    data = parser.Base64MessageToDictionary(message)

    # utils.logToFile(data)

    # handler.Frame(data)

    # handler.LandMarks(data)