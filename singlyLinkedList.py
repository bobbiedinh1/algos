#create the node

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#create the singly list

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

#create def for adding to beginning of list

def addToBeginning(node, sList):
    #if list is empty then the node becomes the head
    if (sList.head==None):
        sList.head = node
        sList.tail = node
    #else the new node.next will follow the current heads address then take its place as the head node
    else:
        node.next = sList.head
        sList.head = node

