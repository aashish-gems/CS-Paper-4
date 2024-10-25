WordArray = []  # Global Array of Integer
NumberOfWords = -1  # Global Integer


# 1c i
def Play():
    global WordArray
    global NumberOfWords
    print("Main word is", WordArray[0])
    YourAnswer = ""  # String
    CorrectAnswers = 0  # Integer
    while YourAnswer != "no":
        Flag = False  # Boolean
        YourAnswer = input("Enter your answer: ")
        for Index in range(1, NumberOfWords + 1):
            if WordArray[Index] == YourAnswer:
                CorrectAnswers = CorrectAnswers + 1
                Flag = True
                WordArray[Index] = ""
                break
        if Flag:
            print("The answer was correct.")
        else:
            print("The answer was incorrect.")
    # 1c ii
    Percentage = int(CorrectAnswers * 10000 / NumberOfWords) / 100
    print("Total correct answers was ", str(Percentage), " %")
    print("Remaining answers")
    for Index in range(1, NumberOfWords + 1):
        if WordArray[Index] != "":
            print(WordArray[Index])


# 1a
def ReadWords(FileName):
    global WordArray
    global NumberOfWords
    try:
        ThisFile = open(FileName, "r")
        ThisLine = (ThisFile.readline()).strip()
        while ThisLine != "":
            WordArray.append(ThisLine)
            NumberOfWords = NumberOfWords + 1
            ThisLine = (ThisFile.readline()).strip()
        ThisFile.close()
    except IOError:
        print("File not found.")
    # 1d i
    Play()


# 1b
YourFile = (input("Enter your difficult level: ")).lower()  # String
if YourFile == "easy":
    ReadWords("Easy.txt")
elif YourFile == "medium":
    ReadWords("Medium.txt")
elif YourFile == "hard":
    ReadWords("Hard.txt")
else:
    print("Invalid difficulty.")
