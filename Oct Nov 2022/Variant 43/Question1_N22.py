# 1a
DataArray = []  # Global Array[0:99] of Integer

# 1b
def ReadFile():
    global DataArray
    try:
        ThisFile = open("IntegerData.txt", "r")
        ThisNum = (ThisFile.readline()).strip()
        while ThisNum != "":
            DataArray.append(int(ThisNum))
            ThisNum = (ThisFile.readline()).strip()
        ThisFile.close()
    except IOError:
        print("File not found")

# 1c
def FindValues():
    global DataArray
    YourNum = -1
    while YourNum < 0 or YourNum > 100:
        try:
            print("Please input a number between 1 to 100")
            YourNum = int(input("Enter your number: "))
        except ValueError:
            YourNum = -1
    Count = 0
    for i in range(len(DataArray)):
        if DataArray[i] == YourNum:
            Count = Count + 1
    return Count


# 1d i
ReadFile()
Answer = FindValues()
print("Your number appeared in the list ", str(Answer), " times")

# 1e
def BubbleSort():
    global DataArray
    NoSwaps = False
    Count = 1
    while not NoSwaps:
        NoSwaps = True
        for i in range(len(DataArray) - Count):
            if DataArray[i] > DataArray[i + 1]:
                Temp = DataArray[i]
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = Temp
                NoSwaps = False
        Count = Count + 1

BubbleSort()
print("Contents of Array after sort")
for j in range(len(DataArray)):
    print(DataArray[j])
