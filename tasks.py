import os
from invoke import task


@task
def proto(c):
    # c.run("protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo.proto")
    # c.run("protoc -I . --python_betterproto_out=indigo_protobuf_betterproto proto/indigo_influx.proto")
    os.chdir("proto")
    c.run("python -m grpc_tools.protoc -I. --python_out=../indigo_protobuf --grpc_python_out=../indigo_protobuf indigo.proto")
    c.run("python -m grpc_tools.protoc -I. --python_out=../indigo_protobuf --grpc_python_out=../indigo_protobuf indigo_influx.proto")
