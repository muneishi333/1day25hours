import datetime
import tkinter as tk
import time
import threading
 
def cal_time():
    ### 無限ループ
    while True:
        #現在時刻取得
        dt_now = datetime.datetime.now()
        hour_24 = dt_now.hour
        min_24  = dt_now.minute
        sec_24  = dt_now.second
        ms_24   = dt_now.microsecond

        #現在時刻を[sec]に変換
        today_totalsec = hour_24*3600 + min_24*60 + sec_24 + float(ms_24)/1000000

        #25hに変換
        x = today_totalsec
        hour_25 = int(x // 3456)
        x -= hour_25*3456
        min_25  = int(x // 57.6)
        x -= min_25*57.6
        sec_25  = int(x // 0.96)
        ms_25   = int((x % 0.96)*1000000)
 
        #時刻設定
        tm = "{:02}:{:02}:{:02}".format(hour_25, min_25, sec_25)
        canvas.delete("all")
        canvas.create_text(100, 50, text=tm, font=(None,36))
 
        #待ち時間
        time.sleep(0.96)

root = tk.Tk()

root.title('25h Clock')

### キャンバス作成
canvas = tk.Canvas(root, width=200, height=100)
 
### キャンバス表示
canvas.pack()
 
### スレッド作成
thread = threading.Thread(target=cal_time, daemon=True)
 
### スレッド開始
thread.start()
 
### イベントループ
canvas.mainloop()
