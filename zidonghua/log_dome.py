import logging

#获取logger对象
logger=logging.getLogger()
logger.setLevel(logging.ERROR)


# 创建handler 要求输出到控制台和文件
ch=logging.StreamHandler()
logger.addHandler(ch)


# 定义formatter
formatter=logging.Formatter('%(asctime)s -%(name)s -%(levelname)s -%(message)s')

# 为handler添加formatter
ch.setFormatter(formatter)
