import json
from typing import Dict, Union, Iterable, List


class ConfigError(Exception):
    def __init__(self, key: str, msg: str):
        self.msg = "Key: {}, Msg: {}".format(key, msg)

    def __str__(self):
        return self.msg


class MPCConfig:
    def __init__(self, self_id: str, addr_dict: Dict[str, str],
                 input_data: Union[str, Iterable[str]], output_data: Union[str, Iterable[str]],
                 executor: str, extra_paras: Dict[str, object], before_exec: List[str], after_exec: List[str]):
        """
        :param self_id:
        :param addr_dict: { id: address(ip: port_compute/port_http }
        :param input_data: input file(s)
        :param output_data: output file(s)
        :param extra_paras: other parameters used
        :param before_exec: operations before executor started
        :param after_exec: operations after executor finished
        """
        self.self_id = self_id
        self.computation_addrs = dict()  # ip:port
        self.query_addrs = dict()  # http(s)://ip:port
        for party_id in addr_dict:
            addr_str = addr_dict[party_id]
            ip, ports = addr_str.split(":")
            port_compute, port_http = ports.split("/")
            self.computation_addrs[party_id] = ip + ":" + port_compute
            self.query_addrs[party_id] = ip + ":" + port_http

        if isinstance(input_data, str):
            input_data = [input_data]
        self.input_data = input_data

        if isinstance(output_data, str):
            output_data = [output_data]
        self.output_data = output_data
        self.extra_paras = extra_paras

        self.executor_name = executor
        self.before_exec = before_exec
        self.after_exec = after_exec

    @staticmethod
    def from_json(file_name: str):
        """
        从JSON文件中读取
        :param file_name:
        :return:
        """
        try:
            config_dict = json.load(open(file_name))
        except Exception as e:
            raise ConfigError("", "Cannot open config file: %s" % e)

        keys = ["self_id", "addr_dict", "input_data", "output_data", "executor", "extra_paras",
                "before_exec", "after_exec"]
        for key in keys:
            if key not in config_dict:
                raise ConfigError(key, "not exist in config file")
        for key in config_dict:
            if key not in keys:
                raise ConfigError(key, "the key is not valid")
        return MPCConfig(**config_dict)

