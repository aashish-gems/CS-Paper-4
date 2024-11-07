# 2a
ArrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]  # Global Array[0:9] of Integer

# 2b i
def LinearSearch(SearchValue):
    global ArrayData
    for Index in range(len(ArrayData)):
        if ArrayData[Index] == SearchValue:
            return True
    return False


# 2b ii
YourValue = int(input("Enter a number to search: "))
if LinearSearch(YourValue):
    print("Found")
else:
    print("Not Found")


# 2c
def BubbleSort():
    global ArrayData
    # Declare Temp: Integer
    for x in range(len(ArrayData) - 1):
        for y in range(len(ArrayData) - x - 1):
            if ArrayData[y] > ArrayData[y + 1]:
                Temp = ArrayData[y]
                ArrayData[y] = ArrayData[y + 1]
                ArrayData[y + 1] = Temp
