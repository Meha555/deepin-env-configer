import os
import yaml
from utils.logger import g_logger
from utils.singleton import singleton

@singleton
class ConfigManager(object):
    """配置文件管理器 单例"""
    def __init__(self, file=None):
        if file is None:
            print('配置文件路径不能为空！')
            return
        self.file = file
        with open(file=file, mode='r+', encoding='utf-8') as f:
            self.handle = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_type:
            g_logger.debug(f"异常信息: {exc_type}: {exc_value}\n{exc_trace}")
            raise(exc_type, exc_value)
        return True

    def __getitem__(self, key: str):
        return self.handle[key]
    def __setitem__(self, key: str, val):
        self.handle[key] = val
    
    def dump(self):
        return self.handle
    
    def read(self, section: str, key: str):
        """读配置文件。目前仅支持一级配置"""
        return self.handle[section][key]
        
    def write(self, section: str, key: str, value):
        """写配置文件。目前仅支持一级配置。应该写入整个文件的json字符串（转为yaml）"""
        self.handle[section][key] = value
        with open(file=self.file, mode='r+', encoding='utf-8') as f:
            (yaml.dump(self.handle, stream=f, allow_unicode=True, default_flow_style=False))
    
if __name__ == "__main__":
    with ConfigManager() as configer:
        version = configer['about']
        print(version)