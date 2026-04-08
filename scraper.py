from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
import subprocess
import config_path
import os
'''
site:www.52av.one
note:有一個外部的N_m3u8DL-RE，替代很慢的ffmpeg，放在檔案根目錄

'''
class GetData:


    def __init__(self,url=None):

        #初始化
        self.url = url
        self.headers = None
        self.soup = None
        self.m3u8_url =None
        self.title = None
        self.url_list = []
        #Run
        self._run()

    def _run(self):

        self._get_m3u8()
        self._download()


    def _get_m3u8(self):


        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True) #[!] True 顯示瀏覽器；True 關閉瀏覽器
            context = browser.new_context()
            page = context.new_page()

            def handle_request(request):
                if '.m3u8?' in request.url and 'yocoo' in request.url:
                    self.m3u8_url = request.url
                    self.url_list.append(self.m3u8_url)

            page.on('request', handle_request) #監聽request
            print('尋找影片地址。。。')

            page.goto('https://www.52av.one/', wait_until='commit', timeout=60000)  # 先拿cookie
            page.goto(self.url, wait_until='domcontentloaded', timeout=60000)  # 再進影片頁
            self._get_title(page.content())

            page.wait_for_timeout(20000) #等待參數，可以在調適
            
            browser.close()
            print('m3u8:', self.m3u8_url)

    def _get_title(self,page=None):
        content = page
        soup = BeautifulSoup(content,'html.parser')
        title = soup.find('title').text.strip()
        self.title = title.split('-')[0].strip()
        print(title)


    def _download(self):

        #init
        url_count = len(self.url_list)

        if not self.m3u8_url:
            print('沒找到m3u8 URL，無法下載')
            return
        if url_count == 1:
            target_url = self.url_list[0]
            output = f'{self.title}.mp4'
            subprocess.run([
            config_path.DOWNLOADER_PATH,  # 跟ffmpeg一樣直接叫名字
            target_url,
            '--save-name', self.title,
            '--save-dir', config_path.DOWNLOAD_FOLDER,  # 目錄參數
            '--thread-count', '8',
            '--auto-select',
            '--download-retry-count',str(10), # 異常後重試次數
            ])
        
        elif url_count > 1:

            print('目標超過一個')
            for i, m3u8 in enumerate(self.url_list, start=1):
                target_url = m3u8
                file_name = f"{self.title}_{i}"
                subprocess.run([
                config_path.DOWNLOADER_PATH,  # 跟ffmpeg一樣直接叫名字
                target_url,
                '--save-name', file_name,
                '--save-dir', config_path.DOWNLOAD_FOLDER,  # 目錄參數
                '--thread-count', '8',
                '--auto-select',
                '--download-retry-count',str(10), # 異常後重試次數
                ])

