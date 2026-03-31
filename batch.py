import re
import config_path
from pathlib import Path

class Batch:


    def __init__(self):

        #初始化
        
        self.target_list = config_path.BATCH_DOWNLOAD_LIST
        self.done_list  = config_path.BATCH_DOWNLOAD_LIST_DONE

        self._check_list()
    def _check_list(self):
        '''
        檢查輸入與完成的list
        '''

        self.target_list.touch(exist_ok=True)
        self.done_list.touch(exist_ok=True)
Batch()