import os
from invoke import task


@task
def proto(c):
    dir="indigo_protobuf"

    c.run("protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo.proto")
    c.run("protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo_influx.proto")
    c.run("python -m grpc_tools.protoc -I. --python_out=indigo_protobuf --grpc_python_out=indigo_protobuf indigo_protobuf/indigo.proto")
    c.run("python -m grpc_tools.protoc -I. --python_out=indigo_protobuf --grpc_python_out=indigo_protobuf indigo_protobuf/indigo_influx.proto")
