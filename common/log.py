import logging
import sys
from config import load_config
from config import conf


def _reset_logger(log):
    for handler in log.handlers:
        handler.close()
        log.removeHandler(handler)
        del handler
    log.handlers.clear()
    log.propagate = True
    appid = conf().get("appid")
    formatter = logging.Formatter(
        "[" + appid + "][%(threadName)s][%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S.%F",
    )

    # console_handle
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(formatter)
    log.addHandler(console_handle)

    # file_handle
    file_handle = logging.FileHandler("./log/" + appid + ".log", encoding="utf-8", mode='a')
    file_handle.setFormatter(formatter)
    log.addHandler(file_handle)


def get_logger(name: str):
    log = logging.getLogger(name)
    _reset_logger(log)
    log.setLevel(logging.INFO)
    return log


# 日志句柄
load_config()
logger = get_logger("log")
