import os 
import time
import random
import subprocess
import sys 

ARGUMENTS = sys.argv

simbols = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
comands = ["Encrypt", "Decrypt", "Clear", "Quit"]
letters = simbols
numberRange = 1

def main():
	ImportKey()
	Decrypt(ARGUMENTS[1], ARGUMENTS[2])

def Decrypt(flag, decFile):

	with open(ARGUMENTS[2], "r") as f:
		text = f.read()
		f.close()

	dataText = ""

	for i in text:
		if (i in letters):
			if (i in letters[-1]):
				dataText += letters[0]
			else:
				i = letters.index(i)  + (int(flag) * numberRange);
				dataText += letters[i]
		else:
			dataText += i

	with open(f"dec_{ARGUMENTS[2]}", "w") as f:
		f.write(dataText)
		f.close()

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

if __name__ == '__main__':
	main()