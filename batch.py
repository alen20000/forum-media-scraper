import re
import config_path
from pathlib import Path
import scraper
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
        檢查輸入與完成的list、下載路徑資料夾，沒有就創建
        '''

        self.target_list.touch(exist_ok=True)
        self.done_list.touch(exist_ok=True)
        self.save_path = config_path.DOWNLOAD_FOLDER #
        path = self.save_path
        path.mkdir(parents=True, exist_ok=True)

    def _read_target_list(self):

        self.content =None
        with open (self.target_list,"r") as f:
            self.content = f.read()

    def _get_urls(self):

        pattern = r"https://www.52av[^\s\"\']+" # 這邊還要優化，最好做到一個soup也能順利提取
        urls = re.findall(pattern,self.content)
        
        done_url = urls.copy() #要複寫的done_list 內容

        for i, url in  enumerate(urls, start=1):
            print(f"目標網址-{i}",url)
            scraper.GetData(url)

            done_url = done_url[1:]
            with open (self.done_list, 'a',encoding='utf-8') as f: # 完成後添加到完成清單
                f.write(f'{url}\n')
            
            with open(self.target_list,'w',encoding='utf-8') as f: #從抓取清單中清除
                f.writelines([line + '\n' for line in done_url])


bd = Batch()