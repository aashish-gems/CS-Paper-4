# 2a i
class Vehicle:
    def __init__(self, ParaID, ParaMaxSpeed, ParaIncreaseAmount):
        self.__ID = ParaID  # String
        self.__MaxSpeed = ParaMaxSpeed  # Integer
        self.__IncreaseAmount = ParaIncreaseAmount  # Integer
        self.__CurrentSpeed = 0  # Integer
        self.__HorizontalPosition = 0  # Integer

# 2a ii
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

# 2a iii
    def SetCurrentSpeed(self, NewCurrentSpeed):
        self.__CurrentSpeed = NewCurrentSpeed

    def SetHorizontalPosition(self, NewHorizontalPosition):
        self.__HorizontalPosition = NewHorizontalPosition

# 2a iv
    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition += self.__CurrentSpeed


# 2b i
class Helicopter(Vehicle):
    def __init__(self, ParaID, ParaMaxSpeed, ParaIncreaseAmount, ParaMaxHeight, ParaVerticalChange):
        Vehicle.__init__(self, ParaID, ParaMaxSpeed, ParaIncreaseAmount)
        self.__MaxHeight = ParaMaxHeight  # Integer
        self.__VerticalChange = ParaVerticalChange  # Integer
        self.__VerticalPosition = 0  # Integer

# 2b ii
    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        Vehicle.IncreaseSpeed(self)
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight


# 2c
def PrintDetails(ToPrint):
    print("Horizontal Position = ", str(ToPrint.GetHorizontalPosition()))
    print("Current Speed = ", str(ToPrint.GetCurrentSpeed()))
    try:
        print("Vertical Position = ", str(ToPrint.GetVerticalPosition()))
    except AttributeError:
        return


# 2d
Car = Vehicle("Tiger", 100, 20)
NewHelicopter = Helicopter("Lion", 350, 40, 100, 3)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
print("Car")
PrintDetails(Car)
print("")

NewHelicopter.IncreaseSpeed()
NewHelicopter.IncreaseSpeed()
print("New Helicopter")
PrintDetails(NewHelicopter)
