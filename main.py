from utils.manager import ConfigManager
from utils.cli import cli_parse


if __name__ == "__main__":
    configer = ConfigManager()
    cli_parse(configer)
    