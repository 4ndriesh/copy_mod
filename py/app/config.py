import os
import yaml
from logging_err import *

class Config:
    __instance = None

    @staticmethod
    def inst():
        if Config.__instance == None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self):
        print('config')
        import sys, os
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, the pyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app
            # path into variable _MEIPASS'.
            self.BASE_DIR =os.getcwd()
        else:
            self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.dir_unpack_out = os.path.join(self.BASE_DIR, 'archive_pack')
        self.dir_unpack_in = os.path.join(self.BASE_DIR, 'archive_unpack')
        for directory in ['archive_pack','archive_unpack']:
            c_dir = os.path.join(self.BASE_DIR, directory)
            if not os.path.exists(c_dir):
                os.makedirs(c_dir)

        self.filename_config = os.path.join(self.BASE_DIR, 'setting.yaml')
        try:
            with open(self.filename_config, 'r') as yaml_config_file:
                self.config = yaml.load(yaml_config_file)
        except Exception as e:
            exeption_print(e)

    @property
    def version(self):
        try:
            return [self.config['version'],self.dir_unpack_out,self.dir_unpack_in ,self.BASE_DIR, self.config['path']]
        except:
            self.config = {'version':'нет версии'}

    @version.setter
    def version(self, value):
        self.config['version'] = value
        with open(self.filename_config, "w") as f:
            yaml.dump(self.config, f,default_flow_style=False)



