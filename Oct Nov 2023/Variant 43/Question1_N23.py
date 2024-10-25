# 1a i
def IterativeVowel(Value):  # String
    # Total: Integer
    # LengthString: Integer
    # FirstCharacter: Char
    Total = 0
    LengthString = len(Value)
    for x in range(LengthString):
        FirstCharacter = Value[0]
        if (FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o"
                or FirstCharacter == "u"):
            Total += 1
        Value = Value[1:len(Value)]
    return Total


# 1a ii
print(IterativeVowel("house"))


# 1b i
def RecursiveVowel(Value):
    # FirstCharacter: Char
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if (FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o"
                or FirstCharacter == "u"):
            return RecursiveVowel(Value[1:len(Value)]) + 1
        else:
            return RecursiveVowel(Value[1:len(Value)])


# 1b ii
print(RecursiveVowel("imagine"))

