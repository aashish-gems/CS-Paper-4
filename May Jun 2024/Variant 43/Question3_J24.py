# 3a
QueueData = [""] * 20  # Global Array[0:19] of Integer
QueueHead = -1  # Global Integer
QueueTail = -1  # Global Integer


# 3b
def Enqueue(DataToAdd):  # String
    global QueueTail, QueueHead, QueueData
    if QueueTail < 19:
        QueueTail += 1
        QueueData[QueueTail] = DataToAdd
        if QueueHead == -1:
            QueueHead += 1
        return True
    return False


# 3c
def Dequeue():
    global QueueTail, QueueHead, QueueData
    if QueueHead > QueueTail or QueueHead == -1:
        return "false"
    else:
        ReturnData = QueueData[QueueHead]
        QueueHead = QueueHead + 1
        return ReturnData


# 3d i
def StoreItems():
    Invalid = 0  # Integer
    for Ask in range(10):
        YourNumber = input("Enter your number: ")
        SumOfProducts = (int(YourNumber[0]) + int(YourNumber[2]) + int(YourNumber[4]) +
                         3 * (int(YourNumber[1]) + int(YourNumber[3]) + int(YourNumber[5])))
        CheckDigit = SumOfProducts // 10
        if CheckDigit == 10:
            CheckDigit = "X"
        if str(CheckDigit) == YourNumber[6]:
            Enqueue(YourNumber[0:6])
        else:
            Invalid += 1
    print("Number of Invalid Outputs: ", str(Invalid))


# 3d ii
StoreItems()
ReturnedValue = Dequeue()  # String
if Dequeue() == "false":
    print("Queue was empty")
else:
    print(ReturnedValue)
