# grpc example / studies / demo

## Setup
1. Install Python3
2. Install Pip
3. Install grpcio and grpcio-tools:
pip3 install grpcio grpcio-tools

---
## Examples

Example 1: ProtoBuff

Example 2: Unary

Example 3: Bidirectional

Example 4: Bidirectional using Stack and asynchronous calls

---

## Refs
Generating protobuff:
python3 -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.

Running server: python3 server_file_name.py

Running client: python3 client_file_name.py

## Special Thanks
SiDi -> Cloud Talks!
