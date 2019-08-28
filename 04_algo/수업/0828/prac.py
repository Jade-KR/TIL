def isFull():
    global rear
    return rear == len(Q)-1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item

def deQueue():
    global front
    if isEmpty():
        print("Queue Empty")
    else:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print("Queue Empty")
    else:
        return Q[front+1]
SIZE = 100
Q = [0]*SIZE
front, rear = -1, -1

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())


# 파이썬 큐
'''
Q = []

Q.append(1)
Q.append(2)
Q.append(3)
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))

'''

#라이브러리 큐
'''
import queue
q = queue.Queue() # 큐 생성
q.put(1) #enQueue
q.put(2)
q.put(3)
print(q.get()) #deQueue
print(q.get())
print(q.get())
'''