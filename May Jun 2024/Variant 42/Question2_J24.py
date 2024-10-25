# 2a i
class Node:
    def __init__(self, ParaLeft, ParaData, ParaRight):
        self.__LeftPointer = ParaLeft  # Integer
        self.__Data = ParaData  # Integer
        self.__RightPointer = ParaRight  # Integer

# 2a ii
    def GetLeft(self):
        return self.__LeftPointer

    def GetData(self):
        return self.__Data

    def GetRight(self):
        return self.__RightPointer

# 2a iii
    def SetLeft(self, UpdateLeft):
        self.__LeftPointer = UpdateLeft

    def SetData(self, UpdateData):
        self.__Data = UpdateData

    def SetRight(self, UpdateRight):
        self.__RightPointer = UpdateRight


# 2b i
class TreeClass:
    def __init__(self):
        self.__FirstNode = -1  # Integer
        self.__NumberNodes = 0  # Integer
        self.__Tree = []  # Array[0:19] of Node
        for Index in range(20):
            self.__Tree.append(Node(-1, -1, -1))

# 2b ii
    def InsertNode(self, ParaNewNode):
        if self.__FirstNode == -1:
            self.__Tree[self.__NumberNodes] = Node(-1, ParaNewNode, -1)
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = Node(-1, ParaNewNode, -1)
            CurrentPointer = self.__FirstNode
            while True:
                PreviousPointer = CurrentPointer
                if self.__Tree[CurrentPointer].GetData() > ParaNewNode:
                    CurrentPointer = self.__Tree[CurrentPointer].GetLeft()
                    if CurrentPointer == -1:
                        self.__Tree[PreviousPointer].SetLeft(self.__NumberNodes)
                        break
                else:
                    CurrentPointer = self.__Tree[CurrentPointer].GetRight()
                    if CurrentPointer == -1:
                        self.__Tree[PreviousPointer].SetRight(self.__NumberNodes)
                        break
        self.__NumberNodes += 1

# 2b iii
    def OutputTree(self):
        if self.__NumberNodes != 0:
            print("Left Ptr  Data  Right Ptr")
            for Index in range(self.__NumberNodes):
                print(self.__Tree[Index].GetLeft(), "       ", self.__Tree[Index].GetData(), "     ",
                      self.__Tree[Index].GetRight())
        else:
            print("No nodes found.")


# 2c i
TheTree = TreeClass()
TheTree.InsertNode(10)
TheTree.InsertNode(11)
TheTree.InsertNode(5)
TheTree.InsertNode(1)
TheTree.InsertNode(20)
TheTree.InsertNode(7)
TheTree.InsertNode(15)
TheTree.OutputTree()
