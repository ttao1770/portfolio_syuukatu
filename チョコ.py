import pyautogui as pgui
import time

pgui.FAILSAFE = True

num = 0
print('0:板を連打')
print('1:購入を連打')

case = int(input())

if case == 0:
	print('何分？')
	mini = int(input())

	for i in range(mini):
		#534=jast1mini
		pgui.hotkey('up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up''up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up','up')


elif case == 1:
	while True:
		pgui.hotkey('space')