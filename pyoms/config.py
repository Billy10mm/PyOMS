import argparse
import ConfigParser

class Config:

    """This will retrieve all params from the config for the provided section heading."""

    def __init__(self, file=False):
        if file:
            self.config_file = file
        else:
            arguments = argparse.ArgumentParser(description='A Python Order Management System', prog='PyOMS')
            arguments.add_argument('--version', action='version', version='%(prog)s 0.1')
            arguments.add_argument('--config', '-c', \
                                   dest='config_file',\
                                   help="PyOMS config file", \
                                   default='pyoms.cfg')
            args = arguments.parse_args()
            self.config_file = args.config_file

        self.config = ConfigParser.ConfigParser()
        self.config.optionxform = str
        self.config.read(self.config_file)

    def get_config_section(self, section):
        """Returns a dictionary of config parameters from the provided section"""
        return dict(self.config.items(section))

    def get_config(self, section, item):
        """Returns a single config value from the provided section and key"""
        return self.config.get(section, item)
