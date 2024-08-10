import sys
import argparse
import json
from utils.manager import ConfigManager as cm

QUIET = False


def cli_parse(tool_cfg = cm('./config/config.yml')):
    # 读命令行参数
    parser = argparse.ArgumentParser(description=f"""deepin环境配置工具 @{tool_cfg['about']['author']} v{tool_cfg['about']['version']}
                                                    {tool_cfg['about']['description']}\n{tool_cfg['about']['git']}"""
                                    , formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version=f"deepin环境配置工具 @{tool_cfg['about']['author']} v{tool_cfg['about']['version']}")
    parser.add_argument('-s', '--show', action='store_false', help='显示详细信息')
    parser.add_argument('-q', '--quiet', action='store_true', help='静默输出')
    parser.add_argument('-t', '--type', type=str, choices=['test', 'dev'], help='配置环境类型', default='dev')
    args = parser.parse_args()
    
    if args.show:
        env_cfg = cm('./config/environment.yml')
        msg = json.dumps(env_cfg.dump(), sort_keys=True, indent=4, separators=(',', ':'))
        print(msg)
    if args.quiet:
        QUIET = True
    if args.type:
        pass
    
    # 把命令行参数值写入配置文件
