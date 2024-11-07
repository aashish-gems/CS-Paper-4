# 2a
class Picture:
    def __init__(self, ParaDescription, ParaWidth, ParaHeight, ParaFrameColour):
        self.__Description = ParaDescription  # String
        self.__Width = ParaWidth  # Integer
        self.__Height = ParaHeight  # Integer
        self.__FrameColour = ParaFrameColour  # String

# 2b
    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour

# 2c
    def SetDescription(self, NewDescription):
        self.__Description = NewDescription


# 2d
PictureList = []  # Array[0:99] of Picture


# 2e
def ReadData():
    try:
        PictureFile = open("Pictures.txt", "r")
        ThisDescription = (PictureFile.readline()).strip()
        Count = 0
        while ThisDescription != "":
            ThisWidth = (PictureFile.readline()).strip()
            ThisHeight = (PictureFile.readline()).strip()
            ThisColour = (PictureFile.readline()).strip()
            PictureList.append(Picture(ThisDescription, int(ThisWidth), int(ThisHeight), ThisColour))
            ThisDescription = (PictureFile.readline()).strip()
            Count = Count + 1
        PictureFile.close()
        return Count
    except IOError:
        print("File not found.")
        return 0


# 2f
ReadData()

# 2g
Colour = (input("Enter the frame colour: ")).lower()
MaxWidth = int(input("Enter the maximum width: "))
MaxHeight = int(input("Enter the maximum height: "))

print("The following pictures meet the criteria:")
for Index in range(len(PictureList)):
    PictureWidth = PictureList[Index].GetWidth()
    PictureHeight = PictureList[Index].GetHeight()
    if PictureWidth < MaxWidth and PictureHeight < MaxHeight and PictureList[Index].GetColour() == Colour:
        print("Description:", PictureList[Index].GetDescription(), "  Width:", PictureWidth, "  Height:", PictureHeight)
