#Spamming tool !

import os
from os import sys
import time
import pyautogui
import pyfiglet

class Utils:

	def clear_all():
		
		if os.name == 'nt':
			os.system('cls')
		elif os.name == 'posix':
			os.system('clear')

	def clean_screen():

		Utils.clear_all()
		
		title = pyfiglet.figlet_format("EZSpam", font="big")
		print(title +'\n', "-" * 43)                

	def error_msg(err_msg):
		
		print(err_msg)
		time.sleep(2.5)
		
	def time_remain():
		
		sec = 10
		
		for i in range(0, sec):
			
			print("\n[*] Time remaining before spamming !", sec)
			time.sleep(1)
			sec = sec - 1
			Utils.clean_screen()
		
class Spam:
	
	def simple_script(message, number, button=None, wait=0):
		
		for i in range(0, number):
			
			if button == None:
			
				pyautogui.typewrite(message + "\n")
				number = number - 1
				print("[*] Spam(s) Remaining:", number)
				time.sleep(wait)
			else:
				pyautogui.press(button)
				pyautogui.typewrite(message + "\n")
				number = number - 1
				print("[*] Spam(s) Remaining:", number)
				time.sleep(wait)				
				
		
		Utils.clean_screen()

class Prog:

	def spam_version(title=None, button=None):
		
		while True:
			
			Utils.clean_screen()
			
			print(title)
			print("\n[1] Fast Spam\n[2] Slow Spam\n[3] Back")
			choose_spam = input("\n[*] Select spam type (1, 2 or 3): ")
			
			if choose_spam == str(3):
				
				Utils.clean_screen()
				break
			
			message = input("\n[*] Message to spam: ")
			number = int(input("\n[*] Number(s) of spam(s): "))
			
			Utils.time_remain()
			
			if choose_spam == str(1):
				
				#Fast spam
				Spam.simple_script(message, number, button)
				
			
			elif choose_spam == str(2):
				
				#Slow spam
				Spam.simple_script(message, number, button, wait=2)

			else:
				Utils.clean_screen()
				Utils.error_msg("[*] Error ! Please select spam type with 1, 2 or 3 !")
				continue
					
	
	def tool_version():
		
		SV = "[*] Simple Version [*]"
		GV = "[*] Games Version [*]"
	
		while True:
			
			print("\n[1] Simple Version\n[2] Games Version\n[3] Exit")
			choose_version = input("\n[*] Select tool version (1, 2 or 3): ")
			
			Utils.clean_screen()
			
			if choose_version == str(1):
				
				Prog.spam_version(title=SV)
			
			elif choose_version == str(2):
				
				bind = input("\n[*] Bind a button for open chat box: ")
				Prog.spam_version(title=GV, button=bind)
			
			elif choose_version == str(3):
				
				Utils.clear_all()
				break
				
			else:
				
				Utils.error_msg("\n[*] Error ! Please select tool version with 1, 2 or 3!")
				Utils.clean_screen()
			 		

	def main_action():
		
		Utils.clean_screen()
		Prog.tool_version()

		
Prog.main_action()
