import time 
import datetime
import random

chars = "+-/*!&%#?=@abcdefghijklnopqrstuvwzABCDEFGHIJKLNOPQRSTUVWZ1234567890"
charsNormal = "!abcdefghijklnopqrstuvwzABCDEFGHIJKLNOPQRSTUVWZ1234567890"

startdate = datetime.datetime.now()
startTime = str(startdate.hour) + str(":") + str(startdate.minute)

longwords = 4
encrypt = ""
decipher = ""
attempt = 0


def Start():
	Encrypt()
	Decipher()
def Encrypt():
	for i in range(longwords):
		global encrypt
		encrypt += random.choice(charsNormal)
def Decipher():
	for i in range(longwords):
		global decipher
		decipher += random.choice(charsNormal)

while True:
	Start()
	date = datetime.datetime.now()
	endTime = str(date.hour) + str(":") + str(date.minute)


	print("=====================")
	print("Encrypt: " + str(encrypt) + "\n")
	print("Decipher: " + str(decipher) + "\n")
	print("=====================")

	if (str(encrypt) == str(decipher)):
		print("# Result #")
		print("Encrypt: " + str(encrypt) + "\n")
		print("Decipher: " + str(decipher) + "\n")
		print("##########")
		with open("result.txt", "a+") as f:
			f.write("============================" + "\n")
			f.write("Encrypt: " + str(encrypt) + "\n")
			f.write("Decipher: " + str(decipher) + "\n")
			f.write("Attempt: " + str(attempt) + "\n")
			f.write("Start time: " + str(startTime) + "\n")
			f.write("End time: " + str(endTime) + "\n")
			f.write("============================" + "\n")
			f.close()

		break
	else:
		encrypt = ""
		decipher = ""
		endTime = ""

	attempt += 1


	#time.sleep(0.5)
