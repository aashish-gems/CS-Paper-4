# 2a i
class Card:
    def __init__(self, ParaNumber, ParaColour):
        self.__Number = ParaNumber  # Number
        self.__Colour = ParaColour  # String

# 2a ii
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

# 2a iii
Red1 = Card(1, "red")
Red2 = Card(2, "red")
Red3 = Card(3, "red")
Red4 = Card(4, "red")
Red5 = Card(5, "red")
Blue1 = Card(1, "blue")
Blue2 = Card(2, "blue")
Blue3 = Card(3, "blue")
Blue4 = Card(4, "blue")
Blue5 = Card(5, "blue")
Yellow1 = Card(1, "yellow")
Yellow2 = Card(2, "yellow")
Yellow3 = Card(3, "yellow")
Yellow4 = Card(4, "yellow")
Yellow5 = Card(5, "yellow")


# 2b i
class Hand:
    def __init__(self, ParaCard1, ParaCard2, ParaCard3, ParaCard4, ParaCard5, ):
        self.__Cards = [ParaCard1, ParaCard2, ParaCard3, ParaCard4, ParaCard5]  # Array[0:4] of Cards
        self.__FirstCard = 0  # Integer
        self.__NumberCards = 5  # Integer

# 2b ii
    def GetCards(self, ParaIndex):
        return self.__Cards[ParaIndex]

# 2b iii
Player1 = Hand(Red1, Red2, Red3, Red4, Yellow1)
Player2 = Hand(Yellow2, Yellow3, Yellow4, Yellow5, Blue1)

# 2c i
def CalculateValue(ThisPlayer):
    Count = 0
    for i in range(5):
        CurrentCard = ThisPlayer.GetCards(i)
        if CurrentCard.GetColour() == "red":
            Count = Count + 5
        elif CurrentCard.GetColour() == "yellow":
            Count = Count + 10
        else:
            Count = Count + 15
        Count = Count + CurrentCard.GetNumber()
    return Count

# 2c ii
Player1Points = CalculateValue(Player1)
Player2Points = CalculateValue(Player2)
if Player1Points > Player2Points:
    print("Player 1 wins!")
elif Player1Points < Player2Points:
    print("Player 2 wins!")
else:
    print("Draw!")
