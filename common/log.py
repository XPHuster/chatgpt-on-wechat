import logging
import sys


def _reset_logger(log):
    for handler in log.handlers:
        handler.close()
        log.removeHandler(handler)
        del handler
    log.handlers.clear()
    log.propagate = False
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    file_handle = logging.FileHandler("run.log", encoding="utf-8")
    file_handle.setFormatter(
        logging.Formatter(
            "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S.%f",
        )
    )
    log.addHandler(file_handle)
    log.addHandler(console_handle)


def get_logger(name: str):
    log = logging.getLogger(name)
    _reset_logger(log)
    log.setLevel(logging.INFO)
    return log


# 日志句柄
logger = get_logger("log")
