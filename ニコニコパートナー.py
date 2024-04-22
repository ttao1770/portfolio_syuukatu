import pyautogui as pgui
import time

#space:営業を開始する
#tab:自動販売機
#up:次の日へ、早送り
#left:一番左の求人
#down:紹介する
#right:裏金
#esc:営業終了

pgui.FAILSAFE = True

while True:
    #space:営業を開始する
    pgui.hotkey("space")
    time.sleep(10)
    pgui.hotkey("down")

    #最初は自動販売機を20秒間連打する
    now = time.time()
    while True:
        pgui.hotkey("tab")
        if (time.time()-now >= 20):
            break
    #一番左の求人を紹介する
    pgui.hotkey("left")

    now = time.time()
    while True:
        pgui.hotkey("tab")
        if (time.time()-now >= 3):
            break
    
    #早送りし自動販売機を10秒間連打する
    pgui.hotkey("up")
    #6人分の求人を処理する
    for i in range(6):
        #自動販売機を10秒間連打する
        now = time.time()
        while True:
            pgui.hotkey("tab")
            if (time.time()-now >= 12):
                break
        
        #一番左の求人を紹介する
        pgui.hotkey("left")
        time.sleep(0.5)

    #次の日
    time.sleep(1)
    pgui.hotkey("up")
    pgui.hotkey("esc")
    time.sleep(14)
    pgui.hotkey("up")
    time.sleep(3)

    #最後に上がった警戒を正常化する
    pgui.hotkey("right")
    time.sleep(10)