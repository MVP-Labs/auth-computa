import grpc
from typing import Dict
from concurrent import futures


class Communicator:
    def __init__(self, self_id: str, addr_dict: Dict[str, str]):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        self.port = addr_dict[self_id].split(":")[1]
        self.server.add_insecure_port('[::]:' + self.port)
        self.server.start()

        self.channels = dict()

        for party in addr_dict:
            if party == self_id:
                continue
            self.channels[party] = grpc.insecure_channel(addr_dict[party])