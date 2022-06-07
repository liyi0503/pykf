import os

# 获取当前文件的路径
config_path = os.path.abspath(__file__)
# 获取config目录
config_dir = os.path.dirname(config_path)
# 获取项目路径
root_dir = os.path.dirname(config_dir)

config_yaml_file = os.path.join(config_dir, "config.yaml")

# print(yaml_file)
