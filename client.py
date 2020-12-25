import zmq
import sys

# ZeroMQ Context
from zmq.utils.strtypes import unicode

context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
sock.send_string(u="hello")
print(sock.recv())