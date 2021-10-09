number = int(input(">> "))

class Borism():
	def __init__(self, free_peace_nexus, minerals: int = 0, nexus: int = 1, time: int = 0):
		self.free_peace_nexus = free_peace_nexus
		self.minerals = minerals
		self.nexus = nexus
		self.time = time

	def buy_nexus(self):
		if (self.minerals >= 400):
			self.free_peace_nexus -= 1
			self.minerals -= 400
			self.nexus += 1	
	def debug_log(self):
			print("\nTime needed :", self.time)
			print("Minerals :", self.minerals)
	def run(self):
		while True:
			self.buy_nexus()
			if (self.free_peace_nexus == 0):
				self.buy_nexus()
				self.debug_log()
				break

			self.minerals += 100 * self.nexus
			self.time += 1

if (__name__ == "__main__"):
	run = Borism(free_peace_nexus = number)
	run.run()
