# 2a
class Balloon:
    def __init__(self, ParaColour, ParaDefenseItem):
        self.__Colour = ParaColour  # String
        self.__DefenseItem = ParaDefenseItem  # String
        self.__Health = 100  # Integer

# 2b
    def GetDefenseItem(self):
        return self.__DefenseItem

# 2c
    def ChangeHealth(self, AddHealth):
        self.__Health += AddHealth

# 2d
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False


# 2e
YourColour = input("Enter your balloon colour: ")
YourDefenseItem = input("Enter your defense item: ")
Balloon1 = Balloon(YourColour, YourDefenseItem)

# 2f
def Defend(ThisBalloon):
    OpponentStrength = int(input("Enter the strength of the opponent: "))
    ThisBalloon.ChangeHealth(-OpponentStrength)
    print("You defended using", ThisBalloon.GetDefenseItem())
    if ThisBalloon.CheckHealth():
        print("You died.")
    else:
        print("You survived.")
    return ThisBalloon

# 2g i
Balloon1 = Defend(Balloon1)
