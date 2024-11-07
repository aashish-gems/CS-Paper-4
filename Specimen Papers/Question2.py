# 2a
class HiddenBox:
    # Private BoxName: String
    # Private Creator: String
    # Private DateHidden: Date
    # Private GameLocation: String
    # Private LastFinds: Array[0:10, 0:1] of String
    # Private Active: Boolean

# 2b
    def __init__(self, ParaBoxName, ParaCreator, ParaDateHidden, ParaGameLocation):
        self.__BoxName = ParaBoxName
        self.__Creator = ParaCreator
        self.__DateHidden = ParaDateHidden
        self.__GameLocation = ParaGameLocation
        self.__LastFinds = [["", ""]] * 10
        self.__Active = False

# 2c
    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


# 2d i
TheBoxes = []  # Array[0:9999] of HiddenBox


# 2d ii
def NewBox():
    YourName = input("Please enter your name: ")
    YourCreator = input("Please enter your creator: ")
    YourDateHidden = input("Please enter your date hidden: ")
    YourGameLocation = input("Please enter your game location: ")
    TheBoxes.append(HiddenBox(YourName, YourCreator, YourDateHidden, YourGameLocation))


# 2d iii
NewBox()


# 2e
class PuzzleBox(HiddenBox):
    # Private PuzzleText: String
    # Private Solution: String
    def __init__(self, ParaBoxName, ParaCreator, ParaDateHidden, ParaGameLocation, ParaPuzzleText, ParaSolution):
        HiddenBox.__init__(self, ParaBoxName, ParaCreator, ParaDateHidden, ParaGameLocation)
        self.__PuzzleText = ParaPuzzleText
        self.__Solution = ParaSolution
