from pathlib import Path


BATH_DIR = Path(__file__).resolve().parent

DOWNLOAD_FOLDER = BATH_DIR / "Downloads"

BATCH_DOWNLOAD_LIST = BATH_DIR / "Bath_Download_List.txt"
BATCH_DOWNLOAD_LIST_DONE = BATH_DIR / "Your_Done_List.txt"



print(BATCH_DOWNLOAD_LIST_DONE)
print(DOWNLOAD_FOLDER)