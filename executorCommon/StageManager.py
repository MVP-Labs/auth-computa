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


class StageManager:
    """
    The StageManager provided a sync method for multiple parties.
    Before a party successfully enter next stage, it will query all other parties to see whether they're ready.
    If one party is not ready, the function next_stage will return False.

    It is for better locating the error when a task is not completed.
    """
    def __init__(self, comm: Union[Communicator, None], logger: logging.Logger):
        """
        :param my_port: port to run Flask server
        :param others_addr: Dict[id, 'http://.../...']
        """
        self.logger = logger

        """
        stage: an integer to mark the current stage of the task. Different remote executors have to sync it.
        """
        self.stage = -1

        """
        status:
        0 not started
        1 running
        2 finished
        3 error
        4 exit (A manager process can make a rpc call to inform the executor to exit)
        """
        self.status = Status.Running

        # Time out for waiting others ready
        self.wait_time = 30

        self.comm = comm

        if comm is not None:
            add_ExecCommServicer_to_server(StageGRPCServicer(self), comm.server)
            self.other_party_stubs = dict()
            for party in comm.channels:
                self.other_party_stubs[party] = ExecCommStub(comm.channels[party])

    def next_stage(self):
        logger = self.logger
        self.stage += 1

        if self.comm is None:
            return True

        not_ready_others = set(self.comm.channels.keys())

        # Doing HTTP(s) queries to make sure every other party is ready
        start_wait_time = time.time()
        while time.time() - start_wait_time <= self.wait_time:
            ready_others = []
            for other in not_ready_others:
                try:
                    stage = self.other_party_stubs[other].GetStage(pb.StageQuery(), timeout=1).stage
                    if stage >= self.stage:
                        ready_others.append(other)
                except Exception as e:
                    logger.warning("next_stage: cannot query {}, the stage server may be not started: {}".format(other, e))
            for ready_other in ready_others:
                not_ready_others.remove(ready_other)
            time.sleep(1)
            if len(not_ready_others) == 0:
                return True
        # Of there are still not ready parties, return False
        logger.error("next_stage: failed due to not ready ones {}".format(not_ready_others))
        return False

    def finish(self, error: bool=False):
        if error:
            self.status = Status.Error
        else:
            self.status = Status.Finished
        return True
