# 2a i
class Horse:
    def __init__(self, ParaName, ParaMaxFenceHeight, ParaPercentageSuccess):
        self.__Name = ParaName  # String
        self.__MaxFenceHeight = ParaMaxFenceHeight  # Integer
        self.__PercentageSuccess = ParaPercentageSuccess  # Integer

# 2a ii
    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

# 2d
    def Success(self, ParaHeight, ParaRisk):
        SuccessArray = [1.0, 0.9, 0.8, 0.7, 0.6]
        if ParaHeight > self.__MaxFenceHeight:
            return 0.2 * self.__PercentageSuccess
        else:
            return SuccessArray[ParaRisk - 1] * self.__PercentageSuccess


# 2b i
Horses = [Horse("Beauty", 150, 72),
          Horse("Jet", 160, 65)]  # Array[0:1] of Horse
print(Horses[0].GetName())
print(Horses[1].GetName())


# 2c i
class Fence:
    def __init__(self, ParaHeight, ParaRisk):
        self.__Height = ParaHeight  # Integer
        self.__Risk = ParaRisk  # Integer

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk


# 2c ii
Courses = []
Index = 0
while Index < 4:
    ThisHeight = int(input("Enter the height of the fence (in cm): "))
    ThisRisk = int(input("Enter the risk of the fence (1 to 5): "))
    if 70 <= ThisHeight <= 180 and 1 <= ThisRisk <= 5:
        Courses.append(Fence(ThisHeight, ThisRisk))
        Index = Index + 1

# 2e i
ChanceList = [0, 0]
for HorseIndex in range(2):
    for FenceIndex in range(4):
        CurrentChance = Horses[HorseIndex].Success(Courses[FenceIndex].GetHeight(), Courses[FenceIndex].GetRisk())
        print("The horse ", Horses[HorseIndex].GetName(), " at fence", FenceIndex + 1, "has a", CurrentChance,
              "% chance of success.")
        ChanceList[HorseIndex] = ChanceList[HorseIndex] + CurrentChance
    ChanceList[HorseIndex] = ChanceList[HorseIndex] / 4
    print("The horse ", Horses[HorseIndex].GetName(), " has an average",
          ChanceList[HorseIndex], "% chance of jumping over all four fences.")


# 2e ii
if ChanceList[0] > ChanceList[1]:
    print("The horse ", Horses[0].GetName(), " has the highest chance of winning.")
else:
    print("The horse ", Horses[1].GetName(), " has the highest chance of winning.")




