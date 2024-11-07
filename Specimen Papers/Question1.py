# 1a
TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]  # Array[0:8] of Integer


# 1b
def InsertionSort():
    global TheData
    for Count in range(len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


# 1c
def OutputData():
    global TheData
    for Index in range(len(TheData)):
        print(TheData[Index])


# 1d i
print("Before Sorting")
OutputData()

InsertionSort()

print("After Sorting")
OutputData()


# 1e i
def SearchData():
    global TheData
    SearchValue = int(input("Enter the Search Value: "))
    for Count in range(len(TheData)):
        if SearchValue == TheData[Count]:
            print("Found")
            return True
    print("Not found")
    return False

SearchData()
