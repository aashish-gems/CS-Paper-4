# 1a i
class EventItem:
    def __init__(self, ParaEventName, ParaType, ParaDifficulty):
        self.__EventName = ParaEventName  # String
        self.__Type = ParaType  # String
        self.__Difficulty = ParaDifficulty  # Integer

# 1a ii
    def GetName(self):
        return self.__EventName

    def GetEventType(self):
        return self.__Type

    def GetDifficulty(self):
        return self.__Difficulty


# 1b i/ii
Group = [EventItem("Bridge", "jump", 3),
         EventItem("Water wade", "swim", 4),
         EventItem("100 mile run", "run", 5),
         EventItem("Gridlock", "dive", 2),
         EventItem("Wall on wall", "jump", 4)]  # Array[0:4] of EventItem

# 1c
class Character:
    def __init__(self, ParaCharacterName, ParaJump, ParaSwim, ParaRun, ParaDive):
        self.__CharacterName = ParaCharacterName  # String
        self.__Jump = ParaJump  # Integer
        self.__Swim = ParaSwim  # Integer
        self.__Run = ParaRun  # Integer
        self.__Dive = ParaDive  # Integer

    def GetName(self):
        return self.__CharacterName

# 1d
    def CalculateScore(self, ThisEventType, ThisDifficulty):
        Compare = None
        if ThisEventType == "jump":
           Compare = self.__Jump
        elif ThisEventType == "swim":
            Compare = self.__Swim
        elif ThisEventType == "run":
            Compare = self.__Run
        elif ThisEventType == "dive":
            Compare = self.__Dive
        if Compare < ThisDifficulty:
            return (5 - ThisDifficulty + Compare) * 20
        else:
            return 100


# 1e i
Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

# 1e ii
TarzScore = 0
for i in range(5):
    CurrentEventName = Group[i].GetName()
    CurrentType = Group[i].GetEventType()
    CurrentDifficulty = Group[i].GetDifficulty()
    if Tarz.CalculateScore(CurrentType, CurrentDifficulty) > Geni.CalculateScore(CurrentType, CurrentDifficulty):
        print("Tarz has won the ", CurrentEventName)
        TarzScore = TarzScore + 1
    elif Tarz.CalculateScore(CurrentType, CurrentDifficulty) < Geni.CalculateScore(CurrentType, CurrentDifficulty):
        print("Geni has won the ", CurrentEventName)
        TarzScore = TarzScore - 1
    else:
        print("The ", CurrentEventName, " is a draw.")

if TarzScore > 0:
    print("Tarz has won the most event for the group.")
elif TarzScore < 0:
    print("Geni has won the most event for the group.")
else:
    print("The overall score was a draw.")




