import json
import os

import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

# Run a simple "Echo" server
while True:
    message = sock.recv_json()
    dic_mess = json.loads(message)
    if dic_mess['command_type'] == 'os':
        command = '{} {}'.format(dic_mess['command_name'], dic_mess['parameters'][0])
        print("the command is {}".format(command))
        result = os.system(command)  # TODo: create the os command convert to a function
    sock.send_json({'result': result})
    print(result)