import scraper
from storage import Storage
from utils.deps import DeployDep

if __name__ == '__main__':


    #初始化
    Storage().create_downloader_folder()
    dev = DeployDep()
    dev.setup_enviroment()
    

    #run
    while True:
        url = input("\n請輸入網址 (或輸入 'q' 離開):\n ")
    
        if url.lower() == 'q':
            print("程式結束。")
            break
        if not url.strip():
            print("網址不能為空，請重新輸入。")
            continue   

        try:

            bot = scraper.GetData(url=url)

        except Exception as e:
            # 這樣萬一其中一個網址報錯，迴圈才不會直接崩潰退出
            print(f"發生錯誤: {e}")
            print("請檢查網址是否正確，或網站是否阻擋了連線。")
    print("按 ENTER 鍵退出")
