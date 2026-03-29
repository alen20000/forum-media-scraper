import scraper
from storage import Storage


if __name__ == '__main__':

    Storage().create_downloader_folder()
    url = input('輸入目標URL:')
    bot = scraper.GetData(url=url)
