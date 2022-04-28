class HanoiStack:
	def __init__(self, SIZE, stack, top):
		self.SIZE = SIZE
		self.stack = stack
		self.top = top
		self.data = None
	def isStackFull(self):
		if (self.top >= self.SIZE - 1):  # 안전한 코드
			return True
		else:
			return False

	def isStackEmpty(self):
		if (self.top <= -1):  # 안전한 코드
			return True
		else:
			return False

	def push(self, value):
		if (self.isStackFull() == True):
			print("Stack is Full!!")
			return
		else:
			self.top = self.top + 1
			self.stack[self.top] = value

	def pop(self):
		if (self.isStackEmpty() == True):
			print("Stack is Empty!!")
			return None
		else:
			self.data = self.stack[self.top]
			self.stack[self.top] = None
			self.top = self.top - 1
			return self.data

SIZE = 5
stackA = ['1', '2', '3', '4', '5']
stackB = []
stackC = []
top = 0

HanoiStackA = HanoiStack(SIZE, stackA, top)
HanoiStackB = HanoiStack(SIZE, stackB, top)
HanoiStackC = HanoiStack(SIZE, stackC, top)

def Hanoi():
	pop_data = HanoiStackA.pop()
	HanoiStackB.push(pop_data)

print(HanoiStackA.stack)
print("return data : ", HanoiStackA.pop())
print(HanoiStackA.stack)
print(HanoiStackB.stack)