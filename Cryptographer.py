import os 

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
comands = ["En", "De", "Cls", "Quit"]

number = 1

def Welcome():
	print ("// Commands //\n")

	for i in comands:
		i = comands.index(i)
		print(" " + str(i) + "." + comands[i])

	print ("\n// Commands //")
	Start()
def Start():
	Type = input("\nEnter type: ")

	if (Type in comands):
		if (Type == "En"):
			Encrypt()
		elif (Type == "De"):
			Decipher()


		elif (Type == "Cls"):
			os.system("cls")
			Welcome()
		elif (Type == "Quit"):
			quit()
	else:
		print("I dont know this command!")
		Start()

def Encrypt():
	global letters

	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in letters):
			if (i in letters[-1]):
				if (i in letters):
					text += letters[0]
			else:
				i = letters.index(i) - number
				text += letters[i]
		elif (i not in letters):
			i = i
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
				if (i in letters):
					text += letters[0]
			else:
				i = letters.index(i) + number
				text += letters[i]
		elif (i not in letters):
			i = i
			text += i

	print(str(text))
	Start()

Welcome()