import webbrowser

answer = input(">>> ")

if (answer == "Song"):
	url = "https://www.youtube.com/watch?v=LE9Q4JN-Yek"
	webbrowser.open(url, new = 0, autoraise = True)
elif (answer == "Class Room"):
	url = "https://classroom.google.com/u/3/h?hl=ru"
	webbrowser.open(url, new = 0, autoraise = True)
elif (answer == "S&CR"):
	Link = ["https://classroom.google.com/u/3/h?hl=ru", "https://www.youtube.com/watch?v=LE9Q4JN-Yek"]
	for url in Link:
		webbrowser.open(url, new = 0, autoraise = True)