# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import executorCommon.Comm.execComm_pb2 as execComm__pb2


class ExecCommStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStage = channel.unary_unary(
        '/ExecComm/GetStage',
        request_serializer=execComm__pb2.StageQuery.SerializeToString,
        response_deserializer=execComm__pb2.Stage.FromString,
        )
    self.GetStatus = channel.unary_unary(
        '/ExecComm/GetStatus',
        request_serializer=execComm__pb2.StatusQuery.SerializeToString,
        response_deserializer=execComm__pb2.Status.FromString,
        )
    self.CallExit = channel.unary_unary(
        '/ExecComm/CallExit',
        request_serializer=execComm__pb2.ExitCall.SerializeToString,
        response_deserializer=execComm__pb2.ExitResult.FromString,
        )


class ExecCommServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetStage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CallExit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExecCommServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStage': grpc.unary_unary_rpc_method_handler(
          servicer.GetStage,
          request_deserializer=execComm__pb2.StageQuery.FromString,
          response_serializer=execComm__pb2.Stage.SerializeToString,
      ),
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=execComm__pb2.StatusQuery.FromString,
          response_serializer=execComm__pb2.Status.SerializeToString,
      ),
      'CallExit': grpc.unary_unary_rpc_method_handler(
          servicer.CallExit,
          request_deserializer=execComm__pb2.ExitCall.FromString,
          response_serializer=execComm__pb2.ExitResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ExecComm', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
