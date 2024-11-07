# 1a
Animals = []  # Global Array[0:9] of String

# 1b
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")


# 1c
def SortDescending():
    global Animals
    # Declare ArrayLength: Integer
    # Declare Temp: String
    ArrayLength = len(Animals)
    for x in range(ArrayLength - 1):
        for y in range(ArrayLength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = Temp


# 1d
SortDescending()
print("List of animals after sorting")
for Index in range(len(Animals)):
    print(Animals[Index])
