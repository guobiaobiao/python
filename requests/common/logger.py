import logging
import time
from  conftest import LOG_DIR

class Logger(object):
    def __init__(self,logger):

        # 创建logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  #指定最低的日志级别级别重低到高logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR

        # 创建handler用于写入 到日志文件
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_name=LOG_DIR + rq + '.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 创建handler用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义formatter为handler添加formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger