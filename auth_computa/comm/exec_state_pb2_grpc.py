# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import exec_state_pb2 as exec__state__pb2


class ExecCommStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStage = channel.unary_unary(
                '/ExecComm/GetStage',
                request_serializer=exec__state__pb2.StageQuery.SerializeToString,
                response_deserializer=exec__state__pb2.Stage.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/ExecComm/GetStatus',
                request_serializer=exec__state__pb2.StatusQuery.SerializeToString,
                response_deserializer=exec__state__pb2.Status.FromString,
                )
        self.CallExit = channel.unary_unary(
                '/ExecComm/CallExit',
                request_serializer=exec__state__pb2.ExitCall.SerializeToString,
                response_deserializer=exec__state__pb2.ExitResult.FromString,
                )


class ExecCommServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallExit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecCommServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStage,
                    request_deserializer=exec__state__pb2.StageQuery.FromString,
                    response_serializer=exec__state__pb2.Stage.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=exec__state__pb2.StatusQuery.FromString,
                    response_serializer=exec__state__pb2.Status.SerializeToString,
            ),
            'CallExit': grpc.unary_unary_rpc_method_handler(
                    servicer.CallExit,
                    request_deserializer=exec__state__pb2.ExitCall.FromString,
                    response_serializer=exec__state__pb2.ExitResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ExecComm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExecComm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ExecComm/GetStage',
            exec__state__pb2.StageQuery.SerializeToString,
            exec__state__pb2.Stage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ExecComm/GetStatus',
            exec__state__pb2.StatusQuery.SerializeToString,
            exec__state__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallExit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ExecComm/CallExit',
            exec__state__pb2.ExitCall.SerializeToString,
            exec__state__pb2.ExitResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
