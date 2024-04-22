import pyautogui as pgui
import time

pgui.FAILSAFE = True

while True:
    pgui.hotkey('space')
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)
    pgui.hotkey('tab')
    time.sleep(1)