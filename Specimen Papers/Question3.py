# 3a
QueueData = [""] * 20  # Array[0:19] of String
FrontPointer = 0  # Integer
EndPointer = 0  # Integer
NumberInQueue = 0  # Integer

# 3b
def Enqueue(DataToAdd):
    global QueueData, FrontPointer, EndPointer, NumberInQueue
    if NumberInQueue == 20:
        return False
    else:
        QueueData[EndPointer] = DataToAdd
        EndPointer = EndPointer + 1
        if EndPointer == 20:
            EndPointer = 0
        NumberInQueue = NumberInQueue + 1
        return True


# 3c
def ReadFile():
    YourFile = input("Enter the file name: ")
    try:
        ThisFile = open(YourFile, "r")
        ThisLine = (ThisFile.readline()).strip()
        AllAdded = True
        while ThisLine != "":
            AllAdded = Enqueue(ThisLine)
            ThisLine = (ThisFile.readline()).strip()
        ThisFile.close()
        if AllAdded:
            return 2
        else:
            return 1
    except IOError:
        return - 1


# 3d i
CaseValue = ReadFile()

if CaseValue == -1:
    print("File not found.")
elif CaseValue == 2:
    print("All data added.")
else:
    print("Queue was full.")


# 3e
def Remove():
    global QueueData, FrontPointer, EndPointer, NumberInQueue
    if NumberInQueue < 2:
        return "No Items"
    else:
        String1 = QueueData[FrontPointer]
        String2 = QueueData[FrontPointer + 1]
        FrontPointer = FrontPointer + 2
        NumberInQueue = NumberInQueue - 2
        return String1 + " " + String2
