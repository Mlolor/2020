import os

PathToSettings = "E:\\Programs\\Xdooms\\"

Components = ["Cpu", "GraphicsCard", "Ozu"]
Commands = ["Components", "Update", "Folder","Clear"]

def Welcome():
	os.system("cls")
	print("== Commands ==\n")
	for i in Commands:
		print(" " + str(Commands.index(i)) + "." + str(i))
	print("\n== Commands ==")
	LoadingSettings()
def LoadingSettings():
	try:
		with open(PathToSettings + "Loader.dat", "r") as f:
			pass
	except:
		try:
			os.mkdir("E:\\Programs\\Xdooms")
		except:
			pass
		with open(PathToSettings + "Loader.dat", "w") as f:
			f.write("// Loader is a TRUE //") 
			f.close()
		for i in Components:
			with open(PathToSettings + str(i) + ".txt", "w") as f:
				f.write("0") 
				f.close()

		LoadingSettings()
	Info()
def Info():
	print("")
	Type = input("Enter type: ")

	if (Type == str(Commands.index("Components"))):
		print("\n==============")
		for i in Components:
			with open(PathToSettings + str(i) + ".txt", "r") as f:
				f = f.read()
			print(str(Components.index(i)) + "." + str(i) + ".txt" + " ==> " + str(f))
		print("==============")
		Info()
	elif (Type == str(Commands.index("Update"))):
		print("\n==============")
		for i in Components:
			print(str(Components.index(i)) + "." + str(i) + ".txt")
		print("==============\n")

		Type = input("Enter number: ")

		if (Type == str(Components.index("Cpu"))):
			NewNum = input("Enter update: ")
			with open(PathToSettings + Components[0] + ".txt", "w") as f:
				f.write(NewNum)
			Info()
		elif (Type == str(Components.index("GraphicsCard"))):
			NewNum = input("Enter update: ")
			with open(PathToSettings + Components[1] + ".txt", "w") as f:
				f.write(NewNum)
			Info()
		elif (Type == str(Components.index("Ozu"))):
			NewNum = input("Enter update: ")
			with open(PathToSettings + Components[2] + ".txt", "w") as f:
				f.write(NewNum)
			Info()
		else:
			print("I dont know this command!")
			Info()
	elif (Type == str(Commands.index("Folder"))):
		os.system("explorer E:\\Programs\\Xdooms")
		print("Opening folder...")
		Info()
	elif (Type == str(Commands.index("Clear"))):
		os.system("cls")
		Welcome()
	else:
		print("I dont know this command!")
		Info()

Welcome()
