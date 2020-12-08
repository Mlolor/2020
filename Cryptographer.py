import os 
import random

simbols = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
comands = ["Encrypt", "Decipher", "Clear", "Quit"]
letters = []
number = 1

def Welcome():
	ImportKey()
	print ("// Commands //\n")

	for i in comands:
		i = comands.index(i)
		print(" " + str(i) + "." + comands[i])

	print ("\n// Commands //")
	Start()
def Start():
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
		Start()

def ImportKey():
	try:
		ReadKey()
	except:
		CreateKey()
		ReadKey()
def ReadKey():
	global letters

	with open("key.txt", "r") as f:
		keySimbols = f.readline()
	letters = []
	for i in keySimbols:
		letters.append(i)
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
	Start()
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
	Start()

Welcome()
