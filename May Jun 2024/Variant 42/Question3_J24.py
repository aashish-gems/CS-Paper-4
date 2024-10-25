# 3a
NumberArray = [100, 85, 644, 22, 15, 8, 1]  # Global Array[0:6] of Integer


# 3b i
# Declare LastItem: Integer
# Declare CheckItem: Integer
# Declare LoopAgain: Boolean
def RecursiveInsertion(IntegerArray, NumberElements):  # Returns Array of Integer
    if NumberElements <= 1:
        return IntegerArray
    else:
        IntegerArray = RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


# 3b ii
NumberArray = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
for Index in range(len(NumberArray)):
    print(NumberArray[Index])


# 3c i
def IterativeInsertion(IntegerArray, NumberElements):  # Returns Array of Integer
    for Count in range(NumberElements):
        LastItem = IntegerArray[Count]
        CurrentPointer = Count - 1
        CheckItem = IntegerArray[CurrentPointer]
        while CurrentPointer != -1 and LastItem < CheckItem:
            IntegerArray[CurrentPointer + 1] = CheckItem
            CheckItem = IntegerArray[CurrentPointer - 1]
            CurrentPointer -= 1
        IntegerArray[CurrentPointer + 1] = LastItem
    return IntegerArray


# 3c ii
IterativeInsertion(NumberArray, len(NumberArray))
print("Iterative")
for List in range(len(NumberArray)):
    print(NumberArray[List])
