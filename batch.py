import re
import config_path
from pathlib import Path

class Batch:


    def __init__(self):

        #初始化
        
        self.target_list = config_path.BATCH_DOWNLOAD_LIST
        self.done_list  = config_path.BATCH_DOWNLOAD_LIST_DONE

        #run
        self._run()

    def _run(self):

        self._check_list()
        self._read_target_list()
        self._get_urls()

    def _check_list(self):
        '''
        檢查輸入與完成的list
        '''

        self.target_list.touch(exist_ok=True)
        self.done_list.touch(exist_ok=True)

    def _read_target_list(self):

        self.content =None
        with open (self.target_list,"r") as f:
            self.content = f.read()

    def _get_urls(self):
        pattern = r"https://www.52av[^\s\"\']+"

        urls = re.findall(pattern,self.content)
        for url in urls:
            print("目標網址",url)
Batch()