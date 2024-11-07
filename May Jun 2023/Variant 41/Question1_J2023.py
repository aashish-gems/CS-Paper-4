# 1a i
DataArray = []  # Array[0:24] of Integer

# 1a ii
try:
    ThisFile = open("Data.txt")
    ThisData = (ThisFile.readline()).strip()
    while ThisData != "":
        DataArray.append(int(ThisData))
        ThisData = (ThisFile.readline()).strip()
    ThisFile.close()
except IOError:
    print("Data file not found")


# 1b i
def PrintArray(OutArray):
    for Index in range(len(OutArray)):
        print(str(OutArray[Index]), end="  ")
    print()


# 1b ii
PrintArray(DataArray)


# 1c
def LinearSearch(SearchArray, SearchValue):
    ArrayLength = len(SearchArray)
    if ArrayLength == 0:
        return 0
    else:
        if SearchArray[0] == SearchValue:
            return LinearSearch(SearchArray[1:ArrayLength], SearchValue) + 1
        else:
            return LinearSearch(SearchArray[1:ArrayLength], SearchValue)


# 1d i
YourNumber = -1
while YourNumber < 0 or YourNumber > 100:
    YourNumber = int(input("Enter a number between 0 and 100 inclusive: "))

CountedResult = LinearSearch(DataArray, YourNumber)
print("The number ", str(YourNumber), " is found ", str(CountedResult), " times.")

