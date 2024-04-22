import pyautogui as pgui
import time

pgui.FAILSAFE = True

#space:鍛冶場
#up:イベント2
#down:イベント1
#right:基底2
#left:基底1
#esc:どっちか
#tab:コイン回収
print("基底：0")
print("イベント：1")
mode = int(input())

num = int(input("鉱脈開放数"))

def event_mode(num):
    if num == 1:
        while True:
            pgui.hotkey("down")
            pgui.hotkey("space")
            pgui.hotkey("tab")
    
    if num == 2:
        while True:
            pgui.hotkey("up")
            pgui.hotkey("down")
            pgui.hotkey("space")
            pgui.hotkey("tab")
    
    if num == 3:
        while True:
            pgui.hotkey("esc")
            pgui.hotkey("up")
            pgui.hotkey("down")
            pgui.hotkey("space")
            pgui.hotkey("tab")

def nomal_mode(num):
    if num == 1:
        while True:
            pgui.hotkey("left")
            pgui.hotkey("space")
            pgui.hotkey("tab")

    if num == 2:
        while True:
            pgui.hotkey("right")
            pgui.hotkey("left")
            pgui.hotkey("space")
            pgui.hotkey("tab")
    
    if num == 3:
        while True:
            pgui.hotkey("esc")
            pgui.hotkey("right")
            pgui.hotkey("left")
            pgui.hotkey("space")
            pgui.hotkey("tab")

def main(mode, num):
    if mode == 0:
        nomal_mode(num)
    
    else :
        event_mode(num)

main(mode, num)