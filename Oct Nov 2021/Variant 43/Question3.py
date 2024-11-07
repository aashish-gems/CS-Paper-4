# 3a
ArrayNodes = [[-1, -1, -1]] * 20  # Array[0:20, 0:2] of Integer
RootPointer = -1  # Integer
FreeNode = 0  # Integer


# 3d
def AddNode():
    global ArrayNodes, FreeNode, RootPointer
    NodeData = int(input("Enter a new number to add: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full.")

# 1c




