# 1a
NameArray = []  # Global Array[0:10] of String
ScoreArray = []  # Global Array[0:10] of Integer

# 1b
def ReadHighScores():
    global NameArray, ScoreArray
    try:
        ScoreFile = open("HighScore.txt", "r")
        ThisName = (ScoreFile.readline()).strip()

        while ThisName != "":
            ThisScore = (ScoreFile.readline()).strip()
            NameArray.append(ThisName)
            ScoreArray.append(int(ThisScore))
            ThisName = (ScoreFile.readline()).strip()

        ScoreFile.close()

    except IOError:
        print("File not found")


# 1c
def OutputHighScores():
    global NameArray, ScoreArray
    for Player in range(len(NameArray)):
        print(NameArray[Player], "   ", ScoreArray[Player])


# 1d i
ReadHighScores()
OutputHighScores()

# 1e i
YourName = ""
while len(YourName) != 3:
    YourName = (input("Enter your name: "))

YourScore = -1

while YourScore < 1 or YourScore > 100000:
    YourScore = int(input("Enter your score: "))

# 1e ii
def AppendHighScore(ThisName, ThisScore):
    global NameArray, ScoreArray

    NameArray.append(ThisName)
    ScoreArray.append(ThisScore)
    CurrentPointer = len(NameArray) - 2

    while CurrentPointer != -1 and ScoreArray[CurrentPointer] < ThisScore:
        NameArray[CurrentPointer + 1] = NameArray[CurrentPointer]
        ScoreArray[CurrentPointer + 1] = ScoreArray[CurrentPointer]
        CurrentPointer -= 1

    NameArray[CurrentPointer + 1] = ThisName
    ScoreArray[CurrentPointer + 1] = ThisScore


# 1e iii
AppendHighScore(YourName, YourScore)
OutputHighScores()

# 1f
def WriteTopTen():
    global NameArray, ScoreArray
    NewFile = open("NewHighScore.txt", "w")

    for Position in range(10):
        NewFile.write(NameArray[Position] + "\n")
        NewFile.write(str(ScoreArray[Position])+ "\n")

    NewFile.close()

# WriteTopTen()
# The question has not said to call the procedure, remove comment and call the procedure to see if it works.
