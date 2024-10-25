# 2a i
Queue = [""] * 50  # Global Array[0:49] of String
HeadPointer = - 1  # Global Integer
TailPointer = 0  # Global Integer


# 2a ii
def Enqueue(DataToAdd):
    global Queue
    global HeadPointer
    global TailPointer
    if not(TailPointer < 50):
        print("Queue is full")
    else:
        Queue[TailPointer] = DataToAdd
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


# 2a iii
def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    if HeadPointer == -1 or HeadPointer > 49:
        print("Queue is empty")
        return "Empty"
    else:
        ReturnElement = Queue[HeadPointer]
        HeadPointer += 1
        return ReturnElement


# 2b i
def ReadData():
    try:
        ThisFile = open("QueueData.txt", "r")
        GameID = (ThisFile.readline()).strip()
        while GameID != "":
            Enqueue(GameID)
            GameID = (ThisFile.readline()).strip()
        ThisFile.close()
    except IOError:
        print("File not found.")


# 2c i
class RecordData:
    def __init__(self, ParaID, ParaTotal):
        self.ID = ParaID  # String
        self.Total = ParaTotal  # Integer


# 2c ii
Records = []  # Global Array[0:49] of RecordData
NumberRecords = 0  # Global Integer


# 2c iii
def TotalData():
    global Records
    global NumberRecords
    # DataAccessed: String
    # Flag: Boolean
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        Flag = True
        NumberRecords += 1
    else:
        for x in range(NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True
    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


# 2d
def OutputRecords():
    global Records
    global NumberRecords
    for Index in range(NumberRecords):
        print("ID: ", Records[Index].ID, "   Total: ", Records[Index].Total)


# 2e i
ReadData()
EndValue = TailPointer - HeadPointer
for Element in range(EndValue):
    TotalData()
OutputRecords()
