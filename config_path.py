from pathlib import Path

#根目錄
BATH_DIR = Path(__file__).resolve().parent

#下載資料夾
DOWNLOAD_FOLDER = BATH_DIR / "Downloads"

#批量清單
BATCH_DOWNLOAD_LIST = BATH_DIR / "Batch_Download_List.txt"
BATCH_DOWNLOAD_LIST_DONE = BATH_DIR / "Your_Done_List.txt"

#m3u8 core
DOWNLOADER_PATH = BATH_DIR / "bin" / "N_m3u8DL-RE.exe"
DEPENDENCIES={
    "N_m3u8DL-RE":{
        "url":"https://github.com/nilaoda/N_m3u8DL-RE/releases/download/v0.5.1-beta/N_m3u8DL-RE_v0.5.1-beta_win-x64_20251029.zip",
        "saving_path":DOWNLOADER_PATH
    }
}

if __name__ =="__main__":
    
    print(BATH_DIR )
    pass