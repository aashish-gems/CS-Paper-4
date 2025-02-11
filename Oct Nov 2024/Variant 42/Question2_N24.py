# 2a
class Queue:
    def __init__(self, ParaQueueArray, ParaHeadPointer, ParaTailPointer):
        self.QueueArray = ParaQueueArray # Array[0:99] of Integer
        self.HeadPointer = ParaHeadPointer  # Integer
        self.TailPointer = ParaTailPointer  # Integer


# 2b
TheQueue = Queue([-1] * 100, -1, 0)

# 2c
def Enqueue(A_Queue, TheData):
    if A_Queue.HeadPointer == -1:
        A_Queue.QueueArray[A_Queue.TailPointer] = TheData
        A_Queue.HeadPointer = 0
        A_Queue.TailPointer = A_Queue.TailPointer + 1
        return A_Queue, 1
    else:
        if A_Queue.TailPointer > 99:
            return A_Queue, -1
        else:
            A_Queue.QueueArray[A_Queue.TailPointer] = TheData
            A_Queue.TailPointer = A_Queue.TailPointer + 1
            return A_Queue, 1

# 2d
def ReturnAllData():
    global TheQueue
    ConcatenatedString = ""
    CurrentPointer = TheQueue.HeadPointer
    while CurrentPointer != TheQueue.TailPointer:
        ConcatenatedString = ConcatenatedString + " " + str(TheQueue.QueueArray[CurrentPointer])
        CurrentPointer = CurrentPointer + 1
    return ConcatenatedString

# 2e i
Count = 0
while True:
    YourInput = int(input("Enter an integer greater than or equal to zero: "))
    if YourInput > -1:
        Count = Count + 1
        AQueue, Flag = Enqueue(TheQueue, YourInput)
    if Count == 10:
        break

print(ReturnAllData())

# 2f
def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer== -1 or TheQueue.HeadPointer == TheQueue.TailPointer:
        return -1
    ReturnValue = TheQueue.QueueArray[TheQueue.HeadPointer]
    TheQueue.HeadPointer = TheQueue.HeadPointer + 1
    return ReturnValue

# 2g i
for i in range(2):
    ThisValue = Dequeue()
    if ThisValue == -1:
        print("Queue is empty.")
    else:
        print(ThisValue)
