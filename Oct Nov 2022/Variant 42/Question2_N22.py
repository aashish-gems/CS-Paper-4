# 2a
class Character:
    def __init__(self, ParaName, ParaX, ParaY):
        self.__ParaName = ParaName  # String
        self.__ParaXCoordinate = ParaX  # Integer
        self.__ParaYCoordinate = ParaY  # Integer

# 2b
    def GetName(self):
        return self.__ParaName

    def GetXCoordinate(self):
        return self.__ParaXCoordinate

    def GetYCoordinate(self):
        return self.__ParaYCoordinate

# 2c
    def ChangePosition(self, XChange, YChange):
        self.__ParaXCoordinate += XChange
        self.__ParaYCoordinate += YChange


# 2d
CharacterList = []  # Array[0:9] of Character

try:
    CharacterFile = open("Characters.txt", "r")
    ThisName = (CharacterFile.readline()).strip()

    while ThisName != "":
        ThisX = (CharacterFile.readline()).strip()
        ThisY = (CharacterFile.readline()).strip()
        CharacterList.append(Character(ThisName, int(ThisX), int(ThisY)))
        ThisName = (CharacterFile.readline()).strip()

    CharacterFile.close()

except IOError:
    print("File not found.")

# 2e
YourNameIndex = -1
YourName = ""
while YourNameIndex == -1:
    YourName = (input("Enter the name of your character: ")).lower()
    for Search in range(len(CharacterList)):
        if (CharacterList[Search].GetName()).lower() == YourName:
            YourNameIndex = Search
            break

Moved = False
while not Moved:
    Moved = True
    YourMove = (input("Enter your direction: ")).upper()
    if YourMove == "A":
        CharacterList[YourNameIndex].ChangePosition(-1, 0)
    elif YourMove == "D":
        CharacterList[YourNameIndex].ChangePosition(1, 0)
    elif YourMove == "W":
        CharacterList[YourNameIndex].ChangePosition(0, 1)
    elif YourMove == "S":
        CharacterList[YourNameIndex].ChangePosition(0, -1)
    else:
        Moved = False
        print("Invalid Move! Try again!")

print(CharacterList[YourNameIndex].GetName(), " has changed Coordinates to X = ",
      CharacterList[YourNameIndex].GetXCoordinate(), "and Y = ", CharacterList[YourNameIndex].GetYCoordinate())
