import os 
import time
import random
import subprocess

simbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
comands = ["Encrypt", "Decipher", "Clear", "Quit"]
letters = ""
number = 1

def Start():
	ImportKey()
	Welcome(logo=True)
def Welcome(logo=False):
	if (logo == True):
		for i in range(6,0,-1):
			print("=======================")
			print("== By vk.comnikita06 ==")
			print("=======================\n")

			print(f"Wait {i} seconds!")
			
			time.sleep(1)
			os.system("cls")

	print ("== Commands ==\n")
	for i in comands:
		i = comands.index(i)
		print(" " + str(i) + "." + comands[i])
	print ("\n== Commands ==")
	Info()
def Info():
	Type = input("\nEnter type: ")

	
	if (Type == str(comands.index("Encrypt"))):
		Encrypt()
	elif (Type == str(comands.index("Decipher"))):
		Decipher()


	elif (Type == str(comands.index("Clear"))):
		os.system("cls")
		Welcome()
	elif (Type == str(comands.index("Quit"))):
		quit()
	else:
		print("I dont know this command!")
		Info()

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
	os.system("cls")
	subprocess.call(["attrib", "+h", "key.txt"])

def Encrypt():
	global letters

	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in letters):
			if (i in letters[0]):
				text += letters[-1]
			else:	
				i = letters.index(i) - number
				text += letters[i]
		else:
			text += i

	print(str(text))
	Info()
def Decipher():
	global letters

	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in letters):
			if (i in letters[-1]):
				text += letters[0]
			else:	
				i = letters.index(i) + number
				text += letters[i]
		else:
			text += i

	print(str(text))
	Info()

Start()
