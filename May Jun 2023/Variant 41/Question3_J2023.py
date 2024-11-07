# 3a
Animal = [""] * 20  # Global Array[0:19] of String
Colour = [""] * 10  # Global Array[0:9] of String
AnimalTopPointer = 0  # Global Integer
ColourTopPointer = 0  # Global Integer


# 3b i
def PushAnimal(DataToPush):
    global Animal, AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True


# 3b ii
def PopAnimal():
    global Animal, AnimalTopPointer
    # ReturnData: String
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


# 3b iii
def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", "r")
        ThisAnimal = (AnimalFile.readline()).strip()
        while ThisAnimal != "":
            PushAnimal(ThisAnimal)
            ThisAnimal = (AnimalFile.readline()).strip()
        AnimalFile.close()
    except IOError:
        print("Animal File not found.")

# 3 v
    try:
        ColourFile = open("ColourData.txt", "r")
        ThisColour = (ColourFile.readline()).strip()
        while ThisColour != "":
            PushColour(ThisColour)
            ThisColour = (ColourFile.readline()).strip()
        ColourFile.close()
    except IOError:
        print("Colour File not found.")


# 3b iv
def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True


def PopColour():
    global Colour, ColourTopPointer
    # ReturnData: String
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


# 3c
def OutputItem():
    PoppedAnimal = PopAnimal()
    PoppedColour = PopColour()
    if PoppedAnimal == "":
        print("No animal")
        PushColour(PoppedColour)
    elif PoppedColour == "":
        print("No colour")
        PushAnimal(PoppedAnimal)
    else:
        print(PoppedColour, " ", PoppedAnimal)


# 3d i
ReadData()
for Index in range(4):
    OutputItem()
