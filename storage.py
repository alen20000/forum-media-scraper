from pathlib import Path


class Storage:


    def __init__(self):
        self.save_path = Path('./Download')

    def create_downloader_folder(self):
        path = self.save_path
        path.mkdir(parents=True, exist_ok=True)