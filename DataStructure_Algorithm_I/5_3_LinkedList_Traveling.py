class Node():
	def __init__(self):
		self.data = None
		self.link = None

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()

node1.data = 30
node2.data = 40
node3.data = 50
node4.data = 60

node1.link = node2
node2.link = node3
node3.link = node4

current = node1

while(current != None):
	print(current.data, end = ' ')
	current = current.link
