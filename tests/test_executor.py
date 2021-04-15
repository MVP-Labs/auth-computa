from executorCommon import Executor
from executorCommon.Utils import parallel
import grpc
from executorCommon.Comm.execComm_pb2_grpc import ExecCommStub
import executorCommon.Comm.execComm_pb2 as pb

ex0 = None
def test_single_executor():
    global ex0
    ex0 = Executor("Res/config0.json", "ex0")
    assert ex0.init()
    assert ex0.next_stage()


def test_multiparty_1():
    ex1 = Executor("Res/config1.json", "ex1")
    ex2 = Executor("Res/config2.json", "ex2")
    ex3 = Executor("Res/config3.json", "ex3")
    outs, errs = parallel([ex1.next_stage, ex2.next_stage, ex3.next_stage])
    assert outs[0] and outs[1] and outs[2]

def test_stage_control():
    control_channel = grpc.insecure_channel("127.0.0.1:12021")
    control_stub = ExecCommStub(control_channel)
    assert control_stub.CallExit(pb.ExitCall()).res == -1
    ex0.stage_manager.finish()
    assert control_stub.CallExit(pb.ExitCall()).res == 0
    assert control_stub.CallExit(pb.ExitCall()).res == 2