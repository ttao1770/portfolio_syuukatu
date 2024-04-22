
import pyautogui as pgui
import time

pgui.FAILSAFE = True

#タスクバーのアクセシビリティを押す
pgui.click(x=1000, y=13, duration=0.5)

#スイッチコントロールを押す
pgui.click(x=1039, y=463, duration=0.5)
time.sleep(1.5)

#スマホに接続する
pgui.click(x=678, y=809, duration=0.5)
time.sleep(3)
pgui.click(x=55, y=809, duration=0.5)
time.sleep(1.5)
pgui.click(x=116, y=808, duration=0.5)
pgui.click(x=100, y=100)

for i in range(10000):
    pgui.hotkey('space')    
    time.sleep(0.5)