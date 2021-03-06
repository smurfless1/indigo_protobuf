# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from indigo_protobuf import indigo_influx_pb2 as indigo__protobuf_dot_indigo__influx__pb2


class InfluxTranslatorStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InfluxSubscribe = channel.unary_stream(
                '/indigo_influx.InfluxTranslator/InfluxSubscribe',
                request_serializer=indigo__protobuf_dot_indigo__influx__pb2.SubscribeArgs.SerializeToString,
                response_deserializer=indigo__protobuf_dot_indigo__influx__pb2.InfluxEvent.FromString,
                )


class InfluxTranslatorServicer(object):
    """Missing associated documentation comment in .proto file"""

    def InfluxSubscribe(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InfluxTranslatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InfluxSubscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.InfluxSubscribe,
                    request_deserializer=indigo__protobuf_dot_indigo__influx__pb2.SubscribeArgs.FromString,
                    response_serializer=indigo__protobuf_dot_indigo__influx__pb2.InfluxEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'indigo_influx.InfluxTranslator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InfluxTranslator(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def InfluxSubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/indigo_influx.InfluxTranslator/InfluxSubscribe',
            indigo__protobuf_dot_indigo__influx__pb2.SubscribeArgs.SerializeToString,
            indigo__protobuf_dot_indigo__influx__pb2.InfluxEvent.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
