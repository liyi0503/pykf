"""
======================
Author: 李轶
Time: 2022/4/20 14:25
Project:读取文件
Company:
======================
"""
from configparser import ConfigParser


class MyConf(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf-8")
