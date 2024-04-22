from multiprocessing.spawn import spawn_main
import pyautogui as pgui
import time
import sys

pgui.FAILSAFE = True

print("0:管理者がついているものを自動化する場合")
print("1:管理者がついていないものを自動化する場合")
print("2:どちらも自動化する場合")
print("3:連打のみ")
print("4:一番上")
print("6:2番上")
print("5:一番下に管理者がついている場合")
mode = input()

print("0:離れない")
print("1:少し離れる")
print("2:寝る")
# print("3:")
# print("4:")
span = input()

if span == '0':
    cool = 18

elif span == '1':
    cool = 10

elif span == '2':
    cool = 0

if mode == '0':
    while True:
        for i in range(100):
            pgui.hotkey('space')
            pgui.hotkey('tab')
        time.sleep(cool)
    
elif mode == '1':
    while True:
        for i in range(100):
            pgui.hotkey('down')
            pgui.hotkey('tab')
        time.sleep(cool)

elif mode == '2':
    while True:
        for i in range(100):
            pgui.hotkey('down')
            pgui.hotkey('space')
            pgui.hotkey('tab')
        time.sleep(cool)

elif mode == '3':
    while True:
        pgui.hotkey('rights')

elif mode == '4':
    while True:
        for i in range(100):
            pgui.hotkey('left')
            pgui.hotkey('tab')
        time.sleep(cool)

elif mode == '5':
    while True:
        for i in range(100):
            pgui.hotkey('right')
            pgui.hotkey('tab')
        time.sleep(cool)

elif mode == '6':
    while True:
        for i in range(100):
            pgui.hotkey('up')
            pgui.hotkey('space')
            pgui.hotkey('tab')
        time.sleep(cool+5)