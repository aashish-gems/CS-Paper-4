# 3a
class Card:
    def __init__(self, ParaNumber, ParaColour):
        self.__Number = ParaNumber  # Integer
        self.__Colour = ParaColour  # String

# 3b
    def GetColour(self):
        return self.__Colour

    def GetNumber(self):
        return self.__Number

# 3c
CardList = [Card(-1, "")] * 30  # Array[0:29] of Card

try:
    CardFile = open("CardValues.txt", "r")
    ThisNumber = (CardFile.readline()).strip()
    Count = 0

    while ThisNumber != "":
        ThisColour = (CardFile.readline()).strip()
        CardList[Count] = Card(int(ThisNumber), ThisColour)
        Count = Count + 1
        ThisNumber = (CardFile.readline()).strip()

    CardFile.close()

except IOError:
    print("File not found.")


# 3d
SelectedCards = []

def ChooseCard():
    global SelectedCards
    YourChoice = -1
    Exit = False
    while not Exit:
        YourChoice = int(input("Choose a number between 1 and 30: "))
        if YourChoice > 0 and not YourChoice > 30:
            Exit = True
            for i in range(len(SelectedCards)):
                if YourChoice == SelectedCards[i]:
                    Exit = False
                    break
    SelectedCards.append(YourChoice)
    return YourChoice

# 3e
Player1 = []  # Array[0:3] of Cards
for j in range(4):
    Player1.append(CardList[ChooseCard() - 1])

for k in range(4):
    print(Player1[k].GetNumber(), Player1[k].GetColour())
