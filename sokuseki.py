import pyautogui as pgui
import time
pgui.FAILSAFE = True

while True:
    pgui.click(x=600, y=272,duration=1)
    #open
    pgui.hotkey('command','o')
    pgui.click(x=71, y=56,duration=0.7)
    pgui.click(x=149, y=12,duration=0.7)
    pgui.click(x=258, y=459,duration=0.3)
    pgui.click(x=851, y=516,duration=1)
    pgui.moveTo(x=10,y=0,duration=0.2)
    pgui.click(x=29, y=54,duration=0.3)
    time.sleep(1)
    pgui.rightClick(x=600, y=272,duration=1)
    pgui.moveTo(x=646, y=339,duration=0.3)
    pgui.click()
    time.sleep(1)