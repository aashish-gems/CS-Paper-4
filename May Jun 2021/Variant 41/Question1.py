# 1a
class Node:
    def __init__(self, ParaData, ParaNextNode):
        self.Data = ParaData  # Integer
        self.NextNode = ParaNextNode  # Integer


# 1b
LinkedList = [Node(1, 1), Node(5, 4), Node(6, 7),
              Node(7, -1), Node(2, 2), Node(0, 6),
              Node(0, 8), Node(56, 3), Node(0, 9),
              Node(0, -1)]  # Array[0:9] of Node

StartPointer = 0  # Integer
EmptyList = 5  # Integer


# 1c i
def OutputNodes(ThisList, ThisStart):
    CurrentPointer = ThisStart
    while CurrentPointer != -1:
        print(ThisList[CurrentPointer].Data)
        CurrentPointer = ThisList[CurrentPointer].NextNode


# 1c ii
OutputNodes(LinkedList, StartPointer)


# 1d i
def AddNode(ThisList, ThisStart, ThisFree):
# When Linked List is full
    if ThisFree == -1:
        return False, ThisList, ThisStart, ThisFree
# When Linked List is not Full
    else:
    # Adding New Node to FreeList
        NewNode = int(input("Enter a new number to add: "))
        ThisList[ThisFree] = Node(NewNode, -1)
    # Changing FreeList Pointer
        NewNodePointer = ThisFree
        ThisFree = ThisList[ThisFree].NextNode
    # When Linked List is empty
        if ThisStart == -1:
            ThisStart = NewNodePointer
    # When LinkedList is not empty
        else:
            CurrentPointer = ThisStart
            PreviousPointer = -1
        # Following the Pointer to find insertion point
            while CurrentPointer != -1:
                PreviousPointer = CurrentPointer
                CurrentPointer = ThisList[CurrentPointer].NextNode
        # Inserting the NewNode at the end
            ThisList[PreviousPointer].NextNode = NewNodePointer
        return True, ThisList, ThisStart, ThisFree


# 1d ii
Result, LinkedList, StartPointer, EmptyList = AddNode(LinkedList, StartPointer, EmptyList)

if Result:
    print("The Node was added.")
else:
    print("The Node was not added.")

OutputNodes(LinkedList, StartPointer)
