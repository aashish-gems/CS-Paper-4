# 1a
def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return Unknown(X - 1, Y) // 2


# 1b i
print("Recursion")

print("Input Values: 10, 15")
print("Return Value: ", Unknown(10, 15))

print("Input Values: 10, 10")
print("Return Value: ", Unknown(10, 10))

print("Input Values: 15, 10")
print("Return Value: ", Unknown(15, 10))


# 1c
def IterativeUnknown(X, Y):
    if X == Y:
        return 1
    else:
        Result = 1
        while X != Y:
            print(X + Y)
            if X < Y:
                Result = Result * 2
                X = X + 1
            else:
                Result = Result // 2
                X = X - 1
        return Result


# 1d i
print("Iterative")

print("Input Values: 10, 15")
print("Return Value: ", IterativeUnknown(10, 15))

print("Input Values: 10, 10")
print("Return Value: ", IterativeUnknown(10, 10))

print("Input Values: 15, 10")
print("Return Value: ", IterativeUnknown(15, 10))
