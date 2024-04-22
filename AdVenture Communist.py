import pyautogui as pgui
import time

pgui.FAILSAFE = True

print('0:自動化済み')
print('1:非自動化')
print('2:アイテム未開放')
print('3:全開放')
print('4:擬似的自動化')
print('5:物資投下のみ')

case = int(input())

print("1:広告を全て見終わった")
print("0:広告を全て見終わってないてない")

adflag = int(input())

print('何分？')
mini = int(input())

if case == 0:
	if adflag == 1:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('tab')
				pgui.hotkey('up')
				time.sleep(0.3)
			time.sleep(1.0)

	elif adflag == 0:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('up')
				time.sleep(0.3)
			time.sleep(1.0)

elif case == 1:
	if adflag == 1:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('tab')
				pgui.hotkey('esc')
				time.sleep(0.3)
			time.sleep(1.0)

	elif adflag == 0:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('esc')
				time.sleep(0.3)
			time.sleep(1.0)


elif case == 2:
	if adflag == 1:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('tab')
				pgui.hotkey('right')
				pgui.hotkey('down')

	elif adflag == 0:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('right')
				pgui.hotkey('down')

elif case == 3:
	if adflag == 1:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('tab')
				pgui.hotkey('down')
				time.sleep(0.3)
			time.sleep(1.0)

	elif adflag == 0:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('down')
				time.sleep(0.3)
			time.sleep(1.0)

elif case ==4:
	if adflag == 1:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('tab')
				pgui.hotkey('right')
			time.sleep(1.0)
		
	elif adflag	== 0:
		for i in range(mini):
			#534=jast1mini
			for i in range(534):
				pgui.hotkey('right')
				time.sleep(0.3)
			time.sleep(1.0)

elif case == 5:
	for i in range(mini):
		#534=jast1mini
		for i in range(534):
			pgui.hotkey('tab')
			time.sleep(0.3)
		time.sleep(1.0)
			