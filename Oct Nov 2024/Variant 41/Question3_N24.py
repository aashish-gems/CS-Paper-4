# 3a
LinkedList = []  # Global Array[0:19, 0:1] of Integer
for Index in range(19):
    LinkedList.append([-1, Index + 1])
LinkedList.append([-1, -1])
FirstEmpty = 0  # Global Integer
FirstNode = -1  # Global Integer

# 3b
def InsertData():
    global FirstEmpty, FirstNode, LinkedList
    for Count in range(5):
        YourData = int(input("Enter a  number to add in Linked List: "))
        if -1 < FirstEmpty < 20:
            CurrentPointer = FirstEmpty
            LinkedList[CurrentPointer][0] = YourData
            FirstEmpty = LinkedList[FirstEmpty][1]
            LinkedList[CurrentPointer][1] = FirstNode
            FirstNode = CurrentPointer

# 3c i
def OutputLinkedList():
    global LinkedList, FirstEmpty, FirstNode
    CurrentPointer = FirstNode
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]

# 3c ii
InsertData()
OutputLinkedList()

# 3d i
def Remove(DataToRemove):
    global LinkedList, FirstEmpty, FirstNode
    CurrentPointer = FirstNode
    PreviousPointer = -1
    while CurrentPointer != -1 and DataToRemove != LinkedList[CurrentPointer][0]:
        PreviousPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer][1]
    if PreviousPointer == -1:
        FirstNode = LinkedList[CurrentPointer][1]
    else:
        LinkedList[PreviousPointer][1] = LinkedList[CurrentPointer][1]
    LinkedList[CurrentPointer][1] = FirstEmpty
    FirstEmpty = CurrentPointer

# 3d ii
print("After")
Remove(5)
OutputLinkedList()