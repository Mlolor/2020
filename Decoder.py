import os 
import time
import random
import subprocess

simbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
comands = ["Encrypt", "Decrypt", "Clear", "Quit"]
letters = simbols
numberRange = 1

def Start():
	for i in range(6,0,-1):
		print("=======================")
		print("==     By Mlolor     ==")
		print("=======================\n")

		print(f"Wait {i} seconds!")
			
		time.sleep(1)
		os.system("cls")
	ImportKey()
	Menu()
def Menu():
	print ("== Commands ==\n")
	for i in comands:
		i = comands.index(i)
		print(" " + str(i) + "." + comands[i])
	print ("\n== Commands ==")
	Menu_Input_Command()
def Menu_Input_Command():
	inputCommand = input("\nEnter type: ")

	if (inputCommand == str(comands.index("Encrypt"))):
		Decrypt(1)
	elif (inputCommand == str(comands.index("Decrypt"))):
		Decrypt(-1)
	elif (inputCommand == str(comands.index("Clear"))):
		os.system("cls")
		Menu()
	elif (inputCommand == str(comands.index("Quit"))):
		quit()
	else:
		print("I dont know this command!")
		Menu_Input_Command()
def Decrypt(dec):
	text = input("Enter text: ")
	dataText = ""

	for i in text:
		if (i in letters):
			if (i in letters[-1]):
				dataText += letters[0]
			else:
				i = letters.index(i)  + (dec * numberRange);
				dataText += letters[i]
		else:
			dataText += i

	print(dataText)
	Menu_Input_Command()

def ImportKey():
	try:
		ReadKey()
	except:
		CreateKey()
		ReadKey()
def ReadKey():
	global letters

	with open("key.txt", "r") as f:
		letters = f.readline()

	os.system("cls")
def CreateKey():
	UsedChar = []
	i = 0

	while True:
		RandomChar = random.choice(simbols)
		if (RandomChar not in UsedChar):
			with open("key.txt", "a") as f:
				f.write(RandomChar)
			UsedChar.append(RandomChar)
			i += 1
		if (i == len(simbols)):
			break
	subprocess.call(["attrib", "+h", "key.txt"])
	os.system("cls")

Start()
