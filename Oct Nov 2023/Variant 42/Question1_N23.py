# 1a i
StackVowel = [""] * 100  # Global Array[0:99] of String
StackConsonant = [""] * 100  # Global Array[0:99] of String

# 1a ii
VowelTop = 0  # Global Integer
ConsonantTop = 0  # Global Integer


# 1b i
def PushData(DataToPush):
    global StackVowel, StackConsonant, VowelTop, ConsonantTop
    if DataToPush == "a" or DataToPush == "e" or DataToPush == "i" or DataToPush == "o" or DataToPush == "u":
        if VowelTop < 100:
            StackVowel[VowelTop] = DataToPush
            VowelTop += 1
        else:
            print("Vowel stack is full.")
    else:
        if ConsonantTop < 100:
            StackConsonant[ConsonantTop] = DataToPush
            ConsonantTop += 1
        else:
            print("Consonant stack is full")


# 1b ii
def ReadData():
    try:
        ThisFile = open("StackData.txt", "r")
        ThisLine = (ThisFile.readline()).strip()
        while ThisLine != "":
            PushData(ThisLine)
            ThisLine = (ThisFile.readline()).strip()
        ThisFile.close()
    except IOError:
        print("File not found.")


# 1c
def PopVowel():
    global StackVowel, VowelTop
    if VowelTop > 0:
        VowelTop -= 1
        return StackVowel[VowelTop]
    return "No data"


def PopConsonant():
    global StackConsonant, ConsonantTop
    if ConsonantTop > 0:
        ConsonantTop -= 1
        return StackConsonant[ConsonantTop]
    return "No data"


# 1d i
ReadData()
Word = ""

while True:
    YourChoice = input("Select your choice (Vowel or Consonant): ")
    if YourChoice.lower() == "vowel":
        ThisLetter = PopVowel()
        if ThisLetter != "No data":
            Word += ThisLetter
        else:
            print("Stack empty")
            break
    elif YourChoice.lower() == "consonant":
        ThisLetter = PopConsonant()
        if ThisLetter != "No data":
            Word += ThisLetter
        else:
            print("Stack empty")
            break
    if len(Word) > 4:
        break

print("Your word is ", Word)
