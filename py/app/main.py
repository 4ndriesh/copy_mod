# -*- coding: utf-8 -*-
__author__ = 'BiziurAA'
import PyQt5.QtQuick
from unpack_arh import unpack
from parser_modul import parser
import os
from config import Config
from qml import qml

setting = Config.inst()

def Main():
    obj_parser = parser()
    if obj_parser.open_url():
        version_file_now = setting.version[0]
        obj_parser.parse_page({"class": "modified"}, {"class": "mod-dwn"})
        link_for_down = obj_parser.get_url_tag()
        web_site, name_file_for_down = os.path.split(link_for_down)
        version_file = obj_parser.get_version()

        archiv_for_unpack = os.path.join(setting.version[1], name_file_for_down)
        if version_file == version_file_now and os.path.exists(setting.version[1]):
            print("Последняя версия файла от {} !!!".format(version_file))
        else:
            setting.version = version_file
            obj_parser.save_file(obj_parser.get_url_tag(), name_file_for_down)

            ua = unpack()
            ua.unpack_rar(archiv_for_unpack, os.path.splitext(name_file_for_down))
            # ua.unpack_archive(archiv_for_unpack, os.path.splitext(name_file_for_down))
            # # del ua
    else:
        print('NO coonecting to url')

    # obj = walk()
    # list_file_for_copy = []
    # for i in obj.get_walk_dbsta(dir_unpack_in):
    #     list_file_for_copy.append(i)
    # return dir_unpack_in

if __name__ == "__main__":

    # sys.exit(qml(*sys.argv))
    Main()
    qml(setting.version[2])
