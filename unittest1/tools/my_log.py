import logging
from lemon.unittest1.tools.project_path import log_path


class Mylog:
    def my_log(self, msg, level):
        # 2、定义一个日志收集器my_logger
        my_logger = logging.getLogger('pyghon11')
        # 3、设定级别
        my_logger.setLevel('DEBUG')
        # 4、设置日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        # 或者formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息%)message)s')
        # 5、创建输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        # 6、两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 7、收集日志
        # my_logger.debug('现在是2019年8月26日')
        # my_logger.error('我想出了把要学习的东西总结出来写在笔记本里的方法')
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)
        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == "__main__":
    my_log = Mylog()
    my_log.debug('我想出了把要学习的东西总结出来写在笔记本里的方法')
