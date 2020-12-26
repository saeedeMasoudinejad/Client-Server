import json

import zmq
import sys

# ZeroMQ Context
from zmq.utils.strtypes import unicode

context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
mes = input()


# def convertor(mes):
#     json_mes = json.loads(mes)
#     “command_type”: “os”,
#     “command_name”: “...”,
#     “parameters”:
#     [
#     “...”,
#     “...”,
#     ]
print(mes)
print(type(mes))

sock.send_json(json.loads(mes))
print(sock.recv_string())
