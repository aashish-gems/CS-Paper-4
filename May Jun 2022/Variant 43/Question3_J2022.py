# 3a
QueueArray = [""] * 10  # Array[0:9] of String
HeadPointer = 0  # Integer
TailPointer = 0  # Integer
NumberInQueue = 0  # Integer

# 3b
def Enqueue(Array, HeadPtr, TailPtr, Num, DataToAdd):
    if Num == 10:
        return False, Array, HeadPtr, TailPtr, Num
    Array[TailPtr] = DataToAdd
    if TailPtr >= 9:
        TailPtr = 0
    else:
        TailPtr += 1
    Num = Num + 1
    return True, Array, HeadPtr, TailPtr, Num


# 3c
def Dequeue(Array, HeadPtr, TailPtr, Num):
    if Num == 0:
        return "FALSE", Array, HeadPtr, TailPtr, Num
    ReturnData = Array[HeadPtr]
    if HeadPtr >= 9:
        HeadPtr = 0
    else:
        HeadPtr = HeadPtr + 1
    Num = Num - 1
    return ReturnData, Array, HeadPtr, TailPtr, Num


# 3d i
for Index in range(11):
    YourInput = input("Enter a string: ")
    Added, QueueArray, HeadPointer, TailPointer, NumberInQueue = Enqueue(QueueArray, HeadPointer,
        TailPointer, NumberInQueue, YourInput)
    if Added:
        print("Successfully added.")
    else:
        print("Failed to add.")


for Index in range(2):
    RetrievedData, QueueArray, HeadPointer, TailPointer, NumberInQueue = Dequeue(QueueArray,
        HeadPointer, TailPointer, NumberInQueue)
    print(RetrievedData)


