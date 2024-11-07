# 2a
class SaleData:
    def __init__(self, ParaID, ParaQuantity):
        self.ID = ParaID  # String
        self.Quantity = ParaQuantity  # Integer


# 2b
CircularQueue = [SaleData("", -1)] * 5  # Global Array[0:4] of SaleData
Head = 0  # Global Integer
Tail = 0  # Global Integer
NumberOfItems = 0  # Global Integer


# 2c
def Enqueue(SaleRecord):
    global CircularQueue, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    CircularQueue[Tail] = SaleRecord
    Tail += 1
    if Tail == 5:
        Tail = 0
    NumberOfItems += 1
    return 1


# 2d
def Dequeue():
    global CircularQueue, Head, NumberOfItems
    if NumberOfItems == 0:
        return SaleData("", -1)
    ReturnRecord = CircularQueue[Head]
    Head += 1
    if Head == 5:
        Head = 0
    NumberOfItems -= 1
    return ReturnRecord


# 2e
def EnterRecord():
    YourID = input("Enter your ID: ")
    YourQuantity = int(input("Enter your Quantity: "))
    if Enqueue(SaleData(YourID, YourQuantity)) == 1:
        print("Stored")
    else:
        print("Full")


# 2f i
for Repeat in range(6):
    EnterRecord()

ExtractedRecord = Dequeue()
if ExtractedRecord.ID == "" and ExtractedRecord.Quantity == -1:
    print("Queue is empty.")
else:
    print("ID: ", ExtractedRecord.ID)
    print("Quantity: ", ExtractedRecord.Quantity)

EnterRecord()
for Index in range(len(CircularQueue)):
    print("ID: ", CircularQueue[Index].ID, "     Quantity: ", CircularQueue[Index].Quantity)
