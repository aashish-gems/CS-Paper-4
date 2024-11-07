# 1a
StackData = [-1] * 10  # Global Array[0:9] of Integer
StackPointer = 0  # Global Integer

# 1b
def OutputStack():
    global StackPointer, StackData
    for i in range(10):
        print(StackData[i])
    print("StackPointer: ", StackPointer)


# 1c
def Push(DataToAdd):
    global StackPointer, StackData
    if StackPointer == 10:
        return False
    StackData[StackPointer] = DataToAdd
    StackPointer = StackPointer + 1
    return True


# 1d i
for Index in range(11):
    YourNumber = int(input("Enter a number: "))
    if Push(YourNumber):
        print("Added")
    else:
        print("Not Added")

OutputStack()


# 1e i
def Pop():
    global StackPointer, StackData
    if StackPointer == 0:
        return -1
    StackPointer = StackPointer - 1
    return StackData[StackPointer]


# 1e ii
Pop()
Pop()

print("Stack after two pops:")
OutputStack()
