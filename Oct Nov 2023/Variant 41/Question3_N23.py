# 3a i
class Character:
    def __init__(self, ParaName, ParaXPosition, ParaYPosition):
        self.__Name = ParaName  # String
        self.__XPosition = ParaXPosition  # Integer
        self.__YPosition = ParaYPosition  # Integer

# 3a ii
    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

# 3a iii
    def SetXPosition(self, IncX):
        self.__XPosition += IncX
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        if self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, IncY):
        self.__YPosition += IncY
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        if self.__YPosition < 0:
            self.__YPosition = 0

# 3a iv
    def Move(self, Command):
        if Command == "up":
            self.SetYPosition(10)
        if Command == "down":
            self.SetYPosition(-10)
        if Command == "right":
            self.SetXPosition(10)
        if Command == "left":
            self.SetXPosition(-10)


# 3b
Jack = Character("Jack", 50, 50)


# 3c i
class BikeCharacter(Character):
    def __init__(self, ParaName, ParaXPosition, ParaYPosition):
        Character.__init__(self, ParaName, ParaXPosition, ParaYPosition)

# 3c ii
    def Move(self, Command):
        Character.Move(self, Command)
        Character.Move(self, Command)


# 3d
Karla = BikeCharacter("karla", 100, 50)

# 3e i
YourCharacter = (input("Select your character (Jack or Karla): ")).lower()
YourMovement = (input("Enter the direction you want to move (up, down, left or right): ")).lower()
if YourCharacter == "jack":
    Jack.Move(YourMovement)
    print("Jack's new position is X = ", str(Jack.GetXPosition()), " Y = ", str(Jack.GetYPosition()))
elif YourCharacter == "karla":
    Karla.Move(YourMovement)
    print("Karla's new position is X = ", str(Karla.GetXPosition()), " Y = ", str(Karla.GetYPosition()))
