# pip
from google.protobuf.json_format import MessageToJson

# global
import base64
import json

# local
from proto import map_segment_pb2

map_metric = map_segment_pb2.map()

def Base64MessageToJSON(data):
    # convert to binarystring
    binaryString = base64.b64decode(data) 
    # parse into a protocol buffer
    map_metric.ParseFromString(binaryString)
    # convert to json and return
    return MessageToJson(map_metric)

def Base64MessageToDictionary(data):
    jsonData = Base64MessageToJSON(data)
    # convert to dictionary and return
    return json.loads(jsonData)

