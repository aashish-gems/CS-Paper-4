# 1a
def ReadData():
    try:
        Items = []  # Array[0:44] of String
        DataFile = open("Data.txt", "r")
        Line = (DataFile.readline()).strip()

        while Line != "":
            Items.append(Line)
            Line = (DataFile.readline()).strip()

        DataFile.close()
        return Items

    except IOError:
        print("File not found.")

# 1b i
def FormatArray(StringList):
    ReturnString = ""
    for Word in range(len(StringList)):
        ReturnString = ReturnString + StringList[Word] + " "
    return ReturnString

# 1b ii
Sentence = FormatArray(ReadData())
print(Sentence)

# 1c
def CompareStrings(String1, String2):
    Index = -1
    while True:
        Index = Index + 1
        if String1[Index] < String2[Index]:
            return 1
        elif String1[Index] > String2[Index]:
            return 2

# 1d i
def Bubble(List):
    for i in range(len(List)):
        for j in range(len(List) - i - 1):
            if CompareStrings(List[j], List[j + 1]) == 2:
                Temp = List[j]
                List[j] = List[j + 1]
                List[j + 1] = Temp
    return List

# 1d ii
print(FormatArray(Bubble(ReadData())))