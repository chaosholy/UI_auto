# encoding=utf-8

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from common.conf import conf
from common.path import log_dir
file_path = os.path.join(log_dir, "log.log")


def create_logger():
    """创建日志收集器"""
    # 1、创建一个收集器
    log = logging.getLogger("lemon")
    log.setLevel(conf("logging", 'level'))  # 设置收集日志的等级

    # 2、创建一个输出到文件的输出渠道(按时间轮转),
    fh = TimedRotatingFileHandler(file_path, when='d', interval=1, backupCount=7, encoding="utf-8")
    fh.setLevel(conf("logging", 'fh_level'))  # 设置输出等级
    log.addHandler(fh)  # 添加到收集器中

    # 3、创建一个输出到控制台的输出渠道
    sh = logging.StreamHandler()
    sh.setLevel(conf('logging', 'sh_level'))  # 设置输出等级
    log.addHandler(sh)  # 添加到收集器中

    # 4、设置日志输出格式
    formatter = "%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s"
    mate = logging.Formatter(formatter)
    fh.setFormatter(mate)
    sh.setFormatter(mate)
    return log


log = create_logger()
