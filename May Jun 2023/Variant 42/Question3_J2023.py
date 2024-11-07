# 3a i
class Employee:
    def __init__(self, ParaHourlyPay, ParaEmployeeNumber, ParaJobTitle):
        self.__HourlyPay = ParaHourlyPay  # Real
        self.__EmployeeNumber = ParaEmployeeNumber  # String
        self.__JobTitle = ParaJobTitle  # String
        self.__PayYear2022 = [0.0] * 52  # Array[0:51] of Real

# 3a ii
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

# 3a iii
    def SetPay(self, ParaWeekNumber, ParaHoursWorked):
        self.__PayYear2022[ParaWeekNumber - 1] = ParaHoursWorked * self.__HourlyPay

# 3a iv
    def GetTotalPay(self):
        TotalPay = 0.0
        for Week in range(52):
            TotalPay = self.__PayYear2022[Week] + TotalPay
        return TotalPay


# 3b i
class Manager(Employee):
    def __init__(self, ParaHourlyPay, ParaEmployeeNumber, ParaJobTitle, ParaBonusValue):
        Employee.__init__(self, ParaHourlyPay, ParaEmployeeNumber,ParaJobTitle)
        self.__BonusValue = ParaBonusValue  # Real

# 3a ii
    def SetPay(self, ParaWeekNumber, ParaHoursWorked):
        Increment = 1 + (self.__BonusValue / 100)
        Employee.SetPay(self, ParaWeekNumber, ParaHoursWorked * Increment)


# 3c
EmployeeArray = []  # Array[0:7] of Employee

try:
    ThisFile = open("Employees.txt", "r")
    Line1 = (ThisFile.readline()).strip()

    while Line1 != "":
        Line2 = (ThisFile.readline()).strip()
        Line3 = (ThisFile.readline()).strip()
        Line4 = (ThisFile.readline()).strip()

        try:
            EmployeeArray.append(Manager(float(Line1), Line2, Line4, float(Line3)))
            Line1 = (ThisFile.readline()).strip()

        except ValueError:
            EmployeeArray.append(Employee(float(Line1), Line2, Line3))
            Line1 = Line4

    ThisFile.close()

except IOError:
    print("File not found.")

# 3d
def EnterHours():
    try:
        HourFile = open("HoursWeek1.txt", "r")
        ThisEmployee = (HourFile.readline()).strip()

        while ThisEmployee != "":
            ThisHour = (HourFile.readline()).strip()

            for Count in range(8):
                if ThisEmployee == EmployeeArray[Count].GetEmployeeNumber():
                    EmployeeArray[Count].SetPay(1, float(ThisHour))
                    break

            ThisEmployee = (HourFile.readline()).strip()
        HourFile.close()
    except IOError:
        print("File not found.")


# 3e
EnterHours()
for Index in range(len(EmployeeArray)):
    print("Employee ID: ", EmployeeArray[Index].GetEmployeeNumber(), " Total Pay: ", EmployeeArray[Index].GetTotalPay())
