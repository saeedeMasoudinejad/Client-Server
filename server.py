import json
import os

import zmq
import subprocess
# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

# Run a simple "Echo" server
while True:
    message = sock.recv_json()
    if message['command_type'] == 'os':
        command = '{} {}'.format(message['command_name'], message['parameters'][0])
        print("the command is {}".format(command))
        proc = subprocess.Popen([message['command_name'], message['parameters'][0]], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        print("the outut is {}".format(out))
        print(type(out))
        # result = os.system(command)  # TODo: create the os command convert to a function
    sock.send_json({'result': out.decode('utf-8')})
    # print(result)





# print "program output:", out