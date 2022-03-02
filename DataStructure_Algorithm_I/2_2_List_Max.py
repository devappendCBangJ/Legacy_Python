originData = [10, 5, 30, 40, 2, 4, 9, 80, 44, 23, 3]
copyData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

max = originData[0]

for i in range(len(originData)):
	if(max < originData[i]):
		max = originData[i]

print(max)