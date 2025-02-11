# 3a
HighScores = []  # Array[0:6, 0:2] of Integer

# 3b
def ReadData():
    MyArray = []
    try:
        ThisFile = open("HighScoreTable.txt")
        ThisID = ThisFile.readline().strip()
        while ThisID != "":
            ThisLevel = ThisFile.readline().strip()
            ThisScore = ThisFile.readline().strip()
            MyArray.append([ThisID, ThisLevel, ThisScore])
            ThisID = ThisFile.readline().strip()
        ThisFile.close()
    except IOError:
        print("File not found.")
    return MyArray

# 3c
def OutputHighScores(Array):
    for i in range(len(Array)):
        print(Array[i][0], " reached level", Array[i][1], " with score of", Array[i][2])

# 3d
def SortScores(ScoreArray):
    for i in range(len(ScoreArray)):
        for j in range(len(ScoreArray) - i - 1):
            if ScoreArray[j][1] * 100 + ScoreArray[j][2] < ScoreArray[j + 1][1] * 100 + ScoreArray[j + 1][2]:
                Temp = ScoreArray[j]
                ScoreArray[j] = ScoreArray[j + 1]
                ScoreArray[j + 1] = Temp
    return ScoreArray

# 3e i
HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
print("After")
HighScores = SortScores(HighScores)
OutputHighScores(HighScores)
