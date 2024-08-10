import logging
import logging.config
import colorlog
import os
import yaml

cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前项目路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')  # log_path为存放日志的路径
if not os.path.exists(log_path):
    os.mkdir(log_path)  # 若不存在logs文件夹，则自动创建

def get_logger(config_file: str = './config/logconf.yml'):
    with open(config_file, "r" ,encoding="utf-8") as f: #注意这里的路径是以shell启动程序时所在的目录决定的
        conf_dict = yaml.safe_load(f)
        logging.config.dictConfig(conf_dict)
        return logging.getLogger()

g_logger = get_logger()