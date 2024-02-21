import os

import logging.handlers

from config import BASE_PATH


class GetLog:
    # 定义类属性保存日志器
    __logger = None

    # 获取日志器 静态方法
    @classmethod
    def get_logger(cls):
        # 如果__logger为空, 无法获取, 需要先创建保存到__logger
        if cls.__logger is None:
            # 创建日志器
            cls.__logger = logging.getLogger("logger")
            # 默认级别
            cls.__logger.setLevel(logging.INFO)
            # 创建处理器
            log_path = BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"
            # 获取处理器
            trfh = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                             when="midnight",
                                                             interval=1,
                                                             backupCount=5,
                                                             encoding="utf-8")
            # 创建格式化器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fmter = logging.Formatter(fmt=fmt)
            # 处理器设置格式
            trfh.setFormatter(fmter)
            # 日志器添加处理器
            cls.__logger.addHandler(trfh)
        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试信息级别日志")
    log.error("测试错误级别")
