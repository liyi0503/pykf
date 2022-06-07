"""
======================
Author: 李轶
Time: 2022/4/20 14:35
Project: 路径获取
Company:
======================
"""
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 拼到配置文件路径
conf_dir = os.path.join(basedir, "config")

# 拼接  测试数据路径
testdata_dir = os.path.join(basedir, "testdatas")

# 日志路径
log_dir = os.path.join(basedir, "outputs", "logs")

# 报告路径
report_dir = os.path.join(basedir, "outputs", "reports")
