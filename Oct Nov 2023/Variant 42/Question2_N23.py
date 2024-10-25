# 2a i
def IterativeCalculate(Number):  # Integer
    # Total: Integer
    # ToFind: Integer
    ToFind = Number
    Total = 0
    while Number != 0:
        if ToFind % Number == 0:
            Total += Number
        Number -= 1
    return Total


# 2a ii
print(IterativeCalculate(10))


# 2b i
def RecursiveCalculate(Number, ToFind):  # Integer, Integer
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveCalculate(Number - 1, ToFind)
        else:
            return RecursiveCalculate(Number - 1, ToFind)


# 2b ii
print(RecursiveCalculate(50, 50))
