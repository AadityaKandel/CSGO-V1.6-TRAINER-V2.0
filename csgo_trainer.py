from ReadWriteMemory import ReadWriteMemory
import struct
from tkinter import *
import keyboard
import time
import tkinter.messagebox as tmsg
import threading
from idlelib.tooltip import Hovertip

root = Tk()
root.title("CSGO TRAINER V2.0")
root.minsize(400,200)
root.maxsize(400,200)
root.iconbitmap("icon\\icon.ico")

# Variables
not_found="CSGO V1.6 NOT FOUND!\nOPEN THE GAME & LAUNCH THE TRAINER AGAIN!!!"
found="CSGO V1.6 FOUND!!\nHAVE FUN WITH YOUR MOD!!"
health="[F7]\t  Toggle Unlimited Health & Money"
info='''CSGO V1.6 TRAINER
'''

# Special Variable
base_address=0x14830000+0x8439E0
game=None
health_detect=False
health_offset = [0x7C, 0x4, 0x320, 0x20, 0x4, 0x4, 0x160]
money_offset = [0x7C, 0x4, 0x320, 0x20, 0x4, 0x1CC]
initial_health = 1120403456
final_health = 1232348160
initial_money = 1000
final_money = 1000000
# Float 100 = 1120403456

def find_process():
	global game
	try:
		game = rm.get_process_by_name('hl.exe')
		game.open()
		return True
	except:
		return False

def detect_process():
	if find_process() == False:
		tmsg.showwarning('Warning',not_found)
		root.destroy()
	else:
		tmsg.showinfo("Success",found)

def modify_health():
	while True:
		if keyboard.is_pressed("f7"):
			time.sleep(0.5)
			while True:
				if keyboard.is_pressed("f7"):
					time.sleep(0.5)
					health_pointer = game.get_pointer(base_address, offsets=health_offset)
					game.write(health_pointer, initial_health)
					money_pointer = game.get_pointer(base_address, offsets=money_offset)
					game.write(money_pointer, initial_money)
					l2.config(fg="white")
					break
				health_pointer = game.get_pointer(base_address, offsets=health_offset)
				game.write(health_pointer, final_health)
				money_pointer = game.get_pointer(base_address, offsets=money_offset)
				game.write(money_pointer, final_money)
				l2.config(fg="green")

# I am LAZY ASF!!! THAT'S WHY I DIDN'T ADD THESE TWO ACTIVATE & DEACTIVATE IN SEPARATE FUNCTIONS> JUST RE-DID THAT $HIT

rm = ReadWriteMemory()


l1 = Label(text=info,fg="white",bg="black",font="comicsansms 10 bold")
l1.pack()

# Health & Money
l2 = Label(text=health,fg="white",bg="black",font="comicsansms 12 italic")

l2.pack(pady=(40,0))

Hovertip(l1,'www.github.com/AADITYAKANDEL')
Hovertip(l2,'Press F7 once and the health & money will remain freezed the entire game')


root.config(bg="black")
detect_process()

t1 = threading.Thread(target=modify_health, daemon=True)

t1.start()

root.mainloop()
