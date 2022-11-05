import sys

ARGUMENTS = sys.argv

def search(oPath, nPath):
	err = 0

	with open(oPath, "r") as f:
		old = f.readlines()
	with open(nPath, "r") as f:
		new = f.readlines()

	size_o = len(old)
	size_n = len(new)

	if (size_o == size_n):
		for i in range(size_o):
			if (old[i] != new[i]):
				print("=" * size_o)
				print(f"line: ({i + 1})\n\n")
				print(f"old:\n{old[i]}")
				print(f"new:\n{new[i]}")
				print("=" * size_o)
				
				err += 1
		return err
if __name__ == '__main__':
	i = search(ARGUMENTS[1], ARGUMENTS[2])

	if (i == 0):
		print("Text has not been changed!")