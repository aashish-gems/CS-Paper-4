# 1a
Jobs = [[]]  # Global Array[0:99, 0:1] of Integers
NumberOfJobs = 0  # Global Integer

# 1b
def Initialise():
    global Jobs, NumberOfJobs
    for ThisIndex in range(100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0


# 1c
def AddJob(ThisJobNumber, ThisJobPriority):
    global Jobs, NumberOfJobs
    if NumberOfJobs == 100:
        print("Not Added")
    else:
        Jobs[NumberOfJobs] = [ThisJobNumber, ThisJobPriority]
        NumberOfJobs += 1
        print("Added")


# 1d
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


# 1e
def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(NumberOfJobs):
        CurrentPointer = i
        JobToInsert = Jobs[CurrentPointer]
        while CurrentPointer != 0 and Jobs[CurrentPointer - 1][1] > JobToInsert[1]:
            Jobs[CurrentPointer] = Jobs[CurrentPointer - 1]
            CurrentPointer = CurrentPointer - 1
        Jobs[CurrentPointer] = JobToInsert

# 1f
def PrintArray():
    global Jobs, NumberOfJobs
    for j in range(NumberOfJobs):
        print(Jobs[j][0], " priority ", Jobs[j][1])


# 1g i
InsertionSort()
PrintArray()
