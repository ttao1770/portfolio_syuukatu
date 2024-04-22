import pyautogui as pgui
import time

pgui.FAILSAFE = True

num = 0
print('0:寝るとき用')

case = int(input())

if case == 0:
	print('何分？')
	mini = int(input())

	for i in range(mini):
		#534=jast1mini
		for i in range(534):
			pgui.hotkey('up')
			time.sleep(0.3)
