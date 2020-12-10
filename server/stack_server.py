from concurrent import futures
import sys
sys.path.insert(0, '../contracts/')
import grpc
import stack_pb2_grpc as stack_pb2_grpc


class StackService(stack_pb2_grpc.BidirectionalServicer):
    stack = []

    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            if message.command == 'PUT':
                StackService.stack.append(message.value)
            elif message.command == 'TOP':
                message.value = StackService.stack[StackService.stack.__len__() -1]
                yield message
            elif message.command == 'GET':
                message.value = str(StackService.stack)
                yield message
            elif message.command == 'POP':
                message.value = StackService.stack.pop()
                yield message
            else:
                message.value = 'Invalid'
                yield message
                


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stack_pb2_grpc.add_BidirectionalServicer_to_server(StackService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()