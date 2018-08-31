
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import os
from logging_err import exeption_print

class parser():
    def __init__(self):
        print('parser')
        pass
    def open_url(self):
        try:
            self.path_to = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'archive_pack')
            self.page = urlopen("http://wotsite.net/pritsely/12214-pritsel-s-uskorennym-svedeniyam-fataliti-dlya-wot.html")
            self.soup = BeautifulSoup(self.page, 'html.parser')
        except Exception as e:
            exeption_print(e)
            return False
        return True
    def parse_page(self,attr1,attr2):
        self.version = self.soup.find(attrs=attr1)
        self.urls_tag = self.soup.find(attrs=attr2)
    def get_version(self):
        return str(self.version.next)
    def get_url_tag(self):
        return self.urls_tag.find('a').get('href')
    def save_file(self,link,name_file_for_down):
        pass
        # urllib.request.urlretrieve(link, os.path.join(self.path_to,name_file_for_down))