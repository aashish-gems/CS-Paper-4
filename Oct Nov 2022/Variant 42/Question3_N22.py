# 3a
Queue = [-1] * 100  # Global Array[0:99] of Integer
HeadPointer = -1
TailPointer = 0

# 3b
def Enqueue(DataToAdd):
    global Queue, TailPointer, HeadPointer
    if TailPointer == 100:
        return False
    Queue[TailPointer] = DataToAdd
    TailPointer += 1
    if HeadPointer == -1:
        HeadPointer = 0
    return True


# 3c
for Insert in range(1, 21):
    if Enqueue(Insert):
        print("Successful")
    else:
        print("Unsuccessful")


# 3d
def RecursiveOutput(Start):
    global Queue, TailPointer, HeadPointer
    if Start == HeadPointer:
        return 0
    return Queue[Start - 1] + RecursiveOutput(Start - 1)


# 3e i
print("Total = ", RecursiveOutput(TailPointer))
