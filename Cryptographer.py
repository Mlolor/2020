import os 

eng = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
ru = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю']
number = 1

def Welcome():
	print("// Commands //\n")
	print("1.EnEng")
	print("2.DeEng")
	print("3.EnRu")
	print("4.DeRu")
	print("5.Cls")
	print("6.Quit")
	print("\n// Commands //")
	Start()

def Start():
	Type = input("\nEnter type: ")


	if (Type == "EnEng"):
		EncryptEng()
	elif (Type == "DeEng"):
		decipherEng()
	if (Type == "EnRu"):
		EncryptRu()
	elif (Type == "DeRu"):
		decipherRu()

	elif (Type == "Cls"):
		os.system("cls")
		Welcome()

	elif (Type == "Quit"):
		quit()
	else:
		print("I dont know this command!")
		Start()

def EncryptEng():
	global eng


	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in eng):
			if (i in eng[-1]):
				text += ru[0]
			else:
				i = eng.index(i) - number
				text += eng[i]
		elif (i not in eng):
			i = i
			text += i
		

	print(str(text))
	Start()
def decipherEng():
	global eng


	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in eng):
			if (i in eng[-1]):
				text += ru[0]
			else:
				i = eng.index(i) + number
				text += eng[i]
		elif (i not in eng):
			i = i
			text += i

	print(str(text))
	Start()

def EncryptRu():
	global ru

	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in ru):
			if (i in ru[-1]):
				text += ru[0]
			else:
				i = ru.index(i) - number
				text += ru[i]
		elif (i not in ru):
			i = i
			text += i
		

	print(str(text))
	Start()
def decipherRu():
	global ru

	message = input("Enter message: ")
	text = ""

	for i in message:
		if (i in ru):
			if (i in ru[-1]):
				text += ru[0]
			else:
				i = ru.index(i) + number
				text += ru[i]
		elif (i not in ru):
			i = i
			text += i

	print(str(text))
	Start()


Welcome()