# 3a
class TreasureChest:
    def __init__(self, ParaQuestion, ParaAnswer, ParaPoints):
        self.__Question = ParaQuestion  # String
        self.__Answer = ParaAnswer  # Integer
        self.__Points = ParaPoints  # Integer

# 3c i
    def GetQuestion(self):
        return self.__Question

# 3c ii
    def CheckAnswer(self, ParaYourAnswer):
        if ParaYourAnswer == self.__Answer:
            return True
        else:
            return False

# 3c iii
    def GetPoints(self, ParaAttempts):
        if ParaAttempts == 1:
            return self.__Points
        elif ParaAttempts == 2:
            return self.__Points // 2
        elif ParaAttempts < 5:
            return self.__Points // 4
        else:
            return 0


# 3b
def ReadData():
    TempArray = []  # Array[0:4] of TreasureChest
    try:
        ChestFile = open("TreasureChestData.txt", "r")
        ThisQuestion = (ChestFile.readline()).strip()
        while ThisQuestion != "":
            ThisAnswer = (ChestFile.readline()).strip()
            ThisPoints = (ChestFile.readline()).strip()
            TempArray.append(TreasureChest(ThisQuestion, int(ThisAnswer), int(ThisPoints)))
            ThisQuestion = (ChestFile.readline()).strip()
        ChestFile.close()
    except IOError:
        print("File not found.")
    return TempArray


# 3c iv
ArrayTreasure = ReadData()

YourNumber = -1
while YourNumber < 1 or YourNumber > 5:
    YourNumber = int(input("Enter a number between 1 and 5: "))

YourQuestion = ArrayTreasure[YourNumber - 1]

print("Your question is:")
print(YourQuestion.GetQuestion())

YourAnswer = int(input("Enter your answer: "))
YourAttempts = 1

while not YourQuestion.CheckAnswer(YourAnswer):
    YourAttempts = YourAttempts + 1
    YourAnswer = int(input("Incorrect answer, try again: "))

print("Your total points is: ", YourQuestion.GetPoints(YourAttempts))
