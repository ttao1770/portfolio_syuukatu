import pyautogui as pgui
import time
from random import randint

# space：次のストーリーを再生
# up：スキップ
# down：最後のスキップ
# right：ストーリー選択からスキップまで
# left：無限ループ回避
# tab：タイトルから復帰

pgui.FAILSAFE = True

while True :
	flag = randint(1,20)
	if flag==3:
		pgui.hotkey('left')
		pgui.hotkey('down')
		time.sleep(8)
		pgui.hotkey('tab')
	pgui.hotkey('space')
	time.sleep(5.5)
	pgui.hotkey('right')
	time.sleep(10.2)
	for i in range(11) :
		pgui.hotkey('up')
		time.sleep(2.3)
		pgui.hotkey('down')
		time.sleep(2.5)
	time.sleep(2.8)