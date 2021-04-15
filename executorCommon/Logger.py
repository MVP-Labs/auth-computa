import logging


logstr_format = '%(levelname)s %(name)s :%(asctime)-15s %(message)s'
logging.basicConfig(filename="log.txt", format=logstr_format)


def get_logger(name: str='executor'):
    return logging.getLogger(name)
