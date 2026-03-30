from pathlib import Path
import config_path

class Storage:


    def __init__(self):
        self.save_path = config_path.DOWNLOAD_FOLDER

    def create_downloader_folder(self):
        path = self.save_path
        path.mkdir(parents=True, exist_ok=True)



