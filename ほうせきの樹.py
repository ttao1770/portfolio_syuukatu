import pyautogui as pgui
import time

pgui.FAILSAFE = True

#leftを起動することで左側の3つのバブルを破壊する
#rightを起動することで右側の3つのバブルを破壊する

print('何分？')
mini = int(input())

for i in range(mini):
    #86s = jast 1 mini
    for j in range(86):
        pgui.hotkey('left')
        pgui.hotkey('right')
    time.sleep(1.0)