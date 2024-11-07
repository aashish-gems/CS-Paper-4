# 3a

ArrayNodes = [[-1, -1, -1]] * 19  # Array[0:19, 0:2] of Integer

# 3b
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]

FreeNode = 6
RootPointer = 0

# 3c
def SearchValues(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValues(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValues(ArrayNodes[Root][2], ValueToFind)

# 3d
def PostOrder(Root):
    global ArrayNodes
    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])
    print(ArrayNodes[Root][1], end=" ")
    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])
    return


# 3e i
MyIndex = SearchValues(RootPointer, 15)
if MyIndex == -1:
    print("The value was not found.")
else:
    print("The value was found at index ", MyIndex)

print("List of values in the tree:")
PostOrder(RootPointer)
