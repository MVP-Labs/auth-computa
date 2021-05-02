import time
import logging
from enum import Enum
from typing import Union

from executorCommon.Comm.Commuicator import Communicator
from executorCommon.Comm.execComm_pb2_grpc import add_ExecCommServicer_to_server, ExecCommServicer, ExecCommStub
import executorCommon.Comm.execComm_pb2 as pb

from executorCommon.Logger import get_logger
from executorCommon.ConfigReader import MPCConfig
from executorCommon.StageManager import StageManager, Status
from executorCommon.Comm.Commuicator import Communicator


class Runner:
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
            add_ExecCommServicer_to_server(
                StageGRPCServicer(self), comm.server)
            self.other_party_stubs = dict()
            for party in comm.channels:
                self.other_party_stubs[party] = ExecCommStub(
                    comm.channels[party])

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
                    stage = self.other_party_stubs[other].GetStage(
                        pb.StageQuery(), timeout=1).stage
                    if stage >= self.stage:
                        ready_others.append(other)
                except Exception as e:
                    logger.warning(
                        "next_stage: cannot query {}, the stage server may be not started: {}".format(other, e))
            for ready_other in ready_others:
                not_ready_others.remove(ready_other)
            time.sleep(1)
            if len(not_ready_others) == 0:
                return True
        # Of there are still not ready parties, return False
        logger.error(
            "next_stage: failed due to not ready ones {}".format(not_ready_others))
        return False

    def finish(self, error: bool = False):
        if error:
            self.status = Status.Error
        else:
            self.status = Status.Finished
        return True


class Executor:
    def __init__(self, config_file: str = "config.json", logger_name: str = "executor"):
        self.logger = get_logger(logger_name)
        try:
            self.config = MPCConfig.from_json(config_file)
        except Exception as e:
            self.logger.error("Read MPCConfig failed: {}".format(e))
            self.finish(error=True)
            return
        try:
            self.comm = Communicator(
                self.config.self_id, self.config.query_addrs)
            self.stage_manager = StageManager(self.comm, self.logger)
        except Exception as e:
            self.logger.error("Initialize communication failed: {}".format(e))
            self.stage_manager = StageManager(None, self.logger)
            self.finish(error=True)
            return

        self.ops = {
            "hello": lambda: print("Hello World")
        }
        self.op_storage = object()
        self.next_stage()

    def _call_op(self, op_name: str):
        if op_name not in self.ops:
            self.logger.error(f"Unrecognized op: {op_name}")
            return False
        else:
            try:
                self.ops[op_name]()
            except Exception as e:
                self.logger.error("Execute op {} error: {}".format(op_name, e))
                return False
        return True

    def next_stage(self):
        if self.stage_manager.next_stage():
            return True
        else:
            self.logger.error(
                "Cannot enter next stage due to at least 1 party is not ready")
            return False

    def init(self):
        if self.stage_manager.status == Status.Error:
            return False
        for op_name in self.config.before_exec:
            if not self._call_op(op_name):
                return False
        return True

    def finish(self, error: bool = False):
        for op_name in self.config.after_exec:
            if not self._call_op(op_name):
                return False
        return self.stage_manager.finish(error)
