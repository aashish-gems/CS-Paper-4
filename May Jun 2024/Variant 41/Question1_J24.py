# 1a
DataSorted = [-1] * 20  # Array[0:19] of Integer
# global NumberItems: Integer


# 1b
def Initialise():
    global DataSorted
    global NumberItems
    YourQuantity = 0  # Integer
    while YourQuantity < 1 or YourQuantity > 20:
        YourQuantity = int(input("Enter quantity of numbers (1 to 20): "))
    for Index in range(YourQuantity):
        DataSorted[Index] = int(input("Enter a number: "))
        NumberItems = NumberItems + 1


# 1c i
NumberItems = 0
Initialise()
print("Before Sorting")
for CountBefore in range(NumberItems):
    print(DataSorted[CountBefore])


# 1d i
def BubbleSort():
    global NumberItems
    global DataSorted
    NoMoreSwaps = False  # Boolean
    LastIndex = NumberItems  # Integer
    while not NoMoreSwaps:
        NoMoreSwaps = True
        LastIndex = LastIndex - 1
        for CurrentPointer in range(LastIndex):
            if DataSorted[CurrentPointer] > DataSorted[CurrentPointer + 1]:
                Temp = DataSorted[CurrentPointer]  # Integer
                DataSorted[CurrentPointer] = DataSorted[CurrentPointer + 1]
                DataSorted[CurrentPointer + 1] = Temp
                NoMoreSwaps = False


# 1d ii
BubbleSort()
print("After Sorting")
for CountAfter in range(NumberItems):
    print(DataSorted[CountAfter])


# 1e i
def BinarySearch(DataToFind):  # Integer
    global NumberItems
    global DataSorted
    Lower = 0  # Integer
    Upper = NumberItems - 1  # Integer
    while True:
        SearchPointer = (Lower + Upper) // 2  # Integer
        if DataSorted[SearchPointer] == DataToFind:
            return SearchPointer
        if Lower > Upper:
            return -1
        if DataSorted[SearchPointer] > DataToFind:
            Upper = SearchPointer - 1
        else:
            Lower = SearchPointer + 1


# 1e ii
YourValue = int(input("Enter a number to search: "))  # Integer
YourIndex = BinarySearch(YourValue)
if YourIndex == -1:
    print("Vale not found.")
else:
    print("Value found at index ", YourIndex)
