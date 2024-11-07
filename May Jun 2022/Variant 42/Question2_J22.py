import random

# 2a
Array = [[-1] * 10 for i in range(10)]  # Array[0:99, 0:99] of Integer

for a in range(10):
    for b in range(10):
        Array[a][b] = random.randint(1, 100)

# 2b i
ArrayLength = 10
for x in range(ArrayLength):
    for y in range(ArrayLength - 1):
        for z in range(ArrayLength - y - 1):
            if Array[x][z] > Array[x][z + 1]:
                TempValue = Array[x][z]
                Array[x][z] = Array[x][z + 1]
                Array[x][z + 1] = TempValue

# 2b ii
for i in range(10):
    for j in range(10):
        print(Array[i][j], end=" ")
    print()

# 2c i
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


# 2c ii
YourNum = int(input("Enter a number: "))
Index = BinarySearch(Array, 0, ArrayLength - 1, YourNum)
if Index == -1:
    print("Value not found.")
else:
    print("Value found at index", Index)

