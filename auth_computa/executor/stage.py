import time
import logging
from enum import Enum
from typing import Union


from executorCommon.Comm.Commuicator import Communicator
from executorCommon.Comm.execComm_pb2_grpc import add_ExecCommServicer_to_server, ExecCommServicer, ExecCommStub
import executorCommon.Comm.execComm_pb2 as pb


class Status(Enum):
    NotStarted = 0
    Running = 1
    Finished = 2
    Error = 3
    Exit = 4


class StageGRPCServicer(ExecCommServicer):
    def __init__(self, istage):
        self.istage = istage

    def GetStage(self, request, context):
        return pb.Stage(stage=self.istage.stage)

    def GetStatus(self, request, context):
        return pb.Status(status=self.istage.status.value)

    def CallExit(self, request, context):
        """
        :param request:
        :param context:
        :return: ExitResult:
                    -  0: exit successfully
                    -  1: exit with error
                    -  2: already exited
                    - -1: not finished
        """
        if self.istage.status == Status.Finished:
            exit_code = 0
            self.istage.status = Status.Exit
        elif self.istage.status == Status.Error:
            exit_code = 1
            self.istage.status = Status.Exit
        elif self.istage.status == Status.Exit:
            exit_code = 2
        else:
            exit_code = -1

        return pb.ExitResult(res=exit_code)
