# 2a i
class Tree:
    def __init__(self, ParaTreeName, ParaHeightGrowth, ParaMaxHeight, ParaMaxWidth, ParaEvergreen):
        self.__TreeName = ParaTreeName  # String
        self.__HeightGrowth = ParaHeightGrowth  # Integer
        self.__MaxHeight = ParaMaxHeight  # Integer
        self.__MaxWidth = ParaMaxWidth  # Integer
        self.__Evergreen = ParaEvergreen  # String

    # 2a ii
    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


# 2b
def ReadData():
    TreeList = []  # Tree
    try:
        ThisFile = open("Trees.txt", "r")
        ThisLine = (ThisFile.readline()).strip()
        while ThisLine != "":
            Previous = 0
            DataList = []
            EndOfLine = len(ThisLine)
            for Index in range(EndOfLine):
                if ThisLine[Index] == ",":
                    DataList.append(ThisLine[Previous:Index])
                    Previous = Index + 1
            DataList.append(ThisLine[Previous:EndOfLine])
            TreeList.append(Tree(DataList[0], int(DataList[1]), int(DataList[2]), int(DataList[3]), DataList[4]))
            ThisLine = (ThisFile.readline()).strip()
        ThisFile.close()
        return TreeList
    except IOError:
        print("File not found.")


# 2c
def PrintTrees(TreeObject):  # Array of Tree
    OutputMessage = (TreeObject.GetTreeName() + " has a maximum height " + str(TreeObject.GetMaxHeight()) +
                     " a maximum width " + str(TreeObject.GetMaxWidth()) + " and grows " +
                     str(TreeObject.GetGrowth()) + " cm a year. ")
    if (TreeObject.GetEvergreen()).lower() == "yes":
        OutputMessage += "It does not lose its leaves."
    else:
        OutputMessage += "It loses its leaves every year."
    print(OutputMessage)


# 2d i
MyTrees = ReadData()
PrintTrees(MyTrees[0])


# 2e i
def ChooseTree(TreeArray):  # Array of Tree
    YourMaxHeight = int(input("Enter the maximum height of your tree in cm: "))
    YourMaxWidth = int(input("Enter the maximum width of your tree in cm: "))
    YourEvergreen = input("Do you want it to be evergreen (Yes/No)? ")
    NumberOfTrees = len(TreeArray)
    YourTrees = []  # Array of Tree
    for ThisTree in range(NumberOfTrees):
        CheckTree = TreeArray[ThisTree]
        HeightReq = CheckTree.GetMaxHeight()
        WidthReq = CheckTree.GetMaxWidth()
        EvergreenReq = CheckTree.GetEvergreen()
        if not (HeightReq > YourMaxHeight or WidthReq > YourMaxWidth or EvergreenReq.lower() != YourEvergreen.lower()):
            PrintTrees(CheckTree)
            YourTrees.append(CheckTree)
    if len(YourTrees) == 0:
        print("There are no suitable trees.")
    else:
        # 2 e ii
        YourPurchase = input("Which tree would you like to buy? ")
        CurrentHeight = int(input("What is the current height in cm when it is bought? "))
        Years = -1
        for Index in range(len(YourTrees)):
            if (YourTrees[Index].GetTreeName()).lower() == YourPurchase.lower():
                Years = (YourTrees[Index].GetMaxHeight() - CurrentHeight) / YourTrees[Index].GetGrowth()
                break
        print("The tree will take ", str(Years), " years to grow to its maximum height.")


# 2e iii
ChooseTree(MyTrees)
