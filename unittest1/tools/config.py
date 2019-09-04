import configparser
from lemon.unittest1.tools.project_path import *


class Config:
    def config(self, file, section, option):
        cf = configparser.ConfigParser()
        cf.read(file, encoding='utf-8')
        return cf.get(section, option)


if __name__ == '__main__':
    print(Config().config(config_path, 'MODE', 'mode'))
