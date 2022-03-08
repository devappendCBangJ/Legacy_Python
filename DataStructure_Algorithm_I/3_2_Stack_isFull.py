def isStackFull():
	global SIZE, stack, top

	if(top >= SIZE - 1):
		return True
	else:
		return False

SIZE = 5
stack = ['A', 'B', 'C', 'D', 'E']
top = 4

print("Check the full statement?", isStackFull())
