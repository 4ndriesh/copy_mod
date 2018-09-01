from pyunpack import Archive
import os
import rarfile
from config import Config

import shutil
class unpack():
    def __init__(self):
        print('unpackr')
        setting = Config.inst()
        self.path_to = os.path.join(setting.version[3],'archive_unpack')
    def mk_dir(self):
        if not os.path.isdir(self.path_to):
            os.makedirs(self.path_to)
    def __del__(self):
        # shutil.rmtree(self.path_to)
        pass
    def unpack_archive(self,path_dir, name_mod):
        make_dir_for_unpack=os.path.join(self.path_to, name_mod[0])
        if not os.path.isdir(make_dir_for_unpack):
            os.makedirs(make_dir_for_unpack)
        Archive(path_dir).extractall(make_dir_for_unpack)
    def unpack_rar(self,path_dir, name_mod):
        rarfile.UNRAR_TOOL = "unrar"
        make_dir_for_unpack = os.path.join(self.path_to, name_mod[0])
        rarfile.RarFile(path_dir).extractall(make_dir_for_unpack)
