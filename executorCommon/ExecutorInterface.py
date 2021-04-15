from executorCommon.Logger import get_logger
from executorCommon.ConfigReader import MPCConfig
from executorCommon.StageManager import StageManager, Status
from executorCommon.Comm.Commuicator import Communicator


class Executor:
    def __init__(self, config_file: str="config.json", logger_name: str="executor"):
        self.logger = get_logger(logger_name)
        try:
            self.config = MPCConfig.from_json(config_file)
        except Exception as e:
            self.logger.error("Read MPCConfig failed: {}".format(e))
            self.finish(error=True)
            return
        try:
            self.comm = Communicator(self.config.self_id, self.config.query_addrs)
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
            self.logger.error("Cannot enter next stage due to at least 1 party is not ready")
            return False

    def init(self):
        if self.stage_manager.status == Status.Error:
            return False
        for op_name in self.config.before_exec:
            if not self._call_op(op_name):
                return False
        return True

    def finish(self, error: bool=False):
        for op_name in self.config.after_exec:
            if not self._call_op(op_name):
                return False
        return self.stage_manager.finish(error)
