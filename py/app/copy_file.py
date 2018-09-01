from timedir import timedir
from datetime import datetime
import shutil
from config import Config
import os
def copy(list_file_for_copy):
    setting = Config.inst()
    gettimedir = timedir()
    gettimedir.timedate = setting.version[4]
    dict_for_copy = gettimedir.timedate
    print(dict_for_copy)
    dict_after_sort = sorted(dict_for_copy, reverse=True)
    for i in dict_after_sort:
        print(datetime.fromtimestamp(i).strftime('%d/%m/%Y'))

    print("-----------------------")
    inc = 0
    for i in range(len(dict_after_sort)):

        if inc == 2: break
        inc += 1
        for files in list_file_for_copy:
            shutil.copy2(os.path.join(files[1],files[2]),os.path.join(setting.version[4],dict_for_copy.get(dict_after_sort[i])))
            # print(datetime.fromtimestamp(dict_after_sort[i]).strftime('%d/%m/%Y'))
            # print(os.path.join(files[1],files[2]))
            # print(os.path.join(setting.version[4],dict_for_copy.get(dict_after_sort[i])))