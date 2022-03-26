def isQueueFull():
    global SIZE, queue, front, rear
    if(rear == SIZE-1):
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("Queue is Full ...")
        return None
    rear += 1
    queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("Queue is empty ...")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ['A', None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print("return data -> ", retData)
print(queue)
retData = deQueue()