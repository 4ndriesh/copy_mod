import os

class timedir():
    dict_for_sorting={}
    @property
    def timedate(self):
            return self.dict_for_sorting

    @timedate.setter
    def timedate(self, scan_dir):
        self.dict_for_sorting.clear()
        for i in os.listdir(scan_dir):
            dir_for_check=os.path.join(scan_dir,i)
            if os.path.isdir(dir_for_check):
                time=os.path.getctime(dir_for_check)
                self.dict_for_sorting.update({time:i})
