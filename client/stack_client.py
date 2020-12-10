from __future__ import print_function

import grpc

import sys
sys.path.insert(0, '../contracts/')

import stack_pb2_grpc as stack_pb2_grpc
import stack_pb2 as stack_pb2


def make_message(command, value):
    return stack_pb2.Message(
        command=command,
        value=value
    )


def generate_messages():
    req = input("[CLIENT] Send command and value:\n").split(',')
    message = make_message(req[0], req[1])
    print("[CLIENT] Command is %s , value is %s" % (req[0], req[1]) )
    yield message


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("[SERVER] Command: %s \t Result: %s " % (response.command, response.value))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = stack_pb2_grpc.BidirectionalStub(channel)
        while True:
            send_message(stub)


if __name__ == '__main__':
    run()