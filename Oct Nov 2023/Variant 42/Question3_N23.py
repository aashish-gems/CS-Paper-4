import datetime


# 3a i
class Character:
    def __init__(self, ParaCharacterName, ParaDateOfBirth, ParaIntelligence, ParaSpeed):
        self.__CharacterName = ParaCharacterName  # String
        self.__DateOfBirth = ParaDateOfBirth  # Date
        self.__Intelligence = ParaIntelligence  # Real
        self.__Speed = ParaSpeed  # Integer

# 3a ii
    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

# 3a iii
    def SetIntelligence(self, NewIntelligence):
        self.__Intelligence = NewIntelligence

# 3a iv
    def Learn(self):
        self.SetIntelligence(self.__Intelligence * 1.1)

# 3a v
    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year


# 3b i
FirstCharacter = Character("Royal", datetime.date(2019, 1, 1), 70, 30)

# 3b ii
FirstCharacter.Learn()
print("Name: ", FirstCharacter.GetName())
print("Age: ", FirstCharacter.ReturnAge())
print("Intelligence: ", FirstCharacter.GetIntelligence())


# 3c i
class MagicCharacter(Character):
    def __init__(self, ParaCharacterName, ParaDateOfBirth, ParaIntelligence, ParaSpeed, ParaElement):
        Character.__init__(self, ParaCharacterName, ParaDateOfBirth, ParaIntelligence, ParaSpeed)
        self.__Element = ParaElement.lower()  # String

# 3c ii
    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            Character.SetIntelligence(self, Character.GetIntelligence(self) * 1.2)
        elif self.__Element == "earth":
            Character.SetIntelligence(self, Character.GetIntelligence(self) * 1.3)
        else:
            Character.Learn(self)


# 3d i
FirstMagic = MagicCharacter("Light", datetime.date(2018, 3, 3), 75, 22, "fire")

# 3d ii
FirstMagic.Learn()
print("Name: ", FirstMagic.GetName())
print("Age: ", FirstMagic.ReturnAge())
print("Intelligence: ", FirstMagic.GetIntelligence())
