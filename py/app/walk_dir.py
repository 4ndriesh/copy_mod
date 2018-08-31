import os
import re
from config import Config

class walk():
    def __init__(self):
        print('walk')
        self.dir_filters = {
            'прицел': re.compile('.*(\.wotmod)$')
        }

    def get_walk_dbsta(self, index_list):
        setting = Config.inst()
        tmp=os.listdir(setting.version[2])
        scan_dir=os.path.join(setting.version[2],tmp[index_list])
        for root, dirs_walk, files in os.walk(scan_dir, topdown=True):
            dirs_walk = [d for d in dirs_walk if d.lower() in self.dir_filters]
            for dir_for_search in dirs_walk:
                for root, dirs_walk, files in os.walk(os.path.join(scan_dir,dir_for_search)):
                    # dirs_walk = [d for d in dirs_walk if d.lower() in self.dir_filters]
                    for d in dirs_walk:
                        key = d.lower()
                        dir = os.path.join(root, d)
                        for f in os.listdir(dir):
                            if os.path.isfile(os.path.join(dir, f)) and self.dir_filters[dir_for_search.lower()].match(f.lower()):
                                yield (key, dir, f)
                            else:
                                dir = os.path.join(dir, f)
                                continue
                return

