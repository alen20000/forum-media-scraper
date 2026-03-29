from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
import subprocess
import os
'''
site:www.52av.one
note:有一個外部的N_m3u8DL-RE，替代很慢的ffmpeg，放在檔案根目錄
'''
class GetData:
    def __init__(self,url=None):
        self.url = url
        self.headers = None
        self.soup = None
        self.m3u8_url =None
        self.title = None
        self.output_dir = 'downloads' #目錄參數，預設根目錄
        self._run()

    def _run(self):

        self._get_m3u8()
        self._download()


    def _get_m3u8(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            def handle_request(request):
                if '.m3u8?' in request.url:
                    self.m3u8_url = request.url
                    print('抓到:', self.m3u8_url)
            page.on('request', handle_request) #監聽request
            print('開始監聽目標')

            page.goto('https://www.52av.one/', wait_until='domcontentloaded', timeout=60000)  # 先拿cookie
            page.goto(self.url, wait_until='domcontentloaded', timeout=60000)  # 再進影片頁
            self._get_title(page.content())

            page.wait_for_timeout(15000) #等待參數，可以在調適
            
            browser.close()
            print('m3u8:', self.m3u8_url)
    def _get_title(self,page=None):
        content = page
        soup = BeautifulSoup(content,'html.parser')
        title = soup.find('title').text.strip()
        self.title = title.split('-')[0].strip()
        print(title)
    def _download(self):
        if not self.m3u8_url:
            print('❌ 沒有 m3u8 URL，無法下載')
            return

        # ① 確保輸出目錄存在
        os.makedirs(self.output_dir, exist_ok=True)

        print(self.output_dir)
        output = f'{self.title}.mp4'
        subprocess.run([
            'N_m3u8DL-RE',  # 跟ffmpeg一樣直接叫名字
            self.m3u8_url,
            '--save-name', self.title,
            '--save-dir', self.output_dir,  # 目錄參數
            '--thread-count', '16',
            '--auto-select',
        ])
url = input('輸入目標URL:')
if __name__ == '__main__':
    bot = GetData(url=url)
