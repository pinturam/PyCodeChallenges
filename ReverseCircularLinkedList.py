# Program to create a Circular Linked List of n nodes and display it in reverse order

# Creat a node of list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Circular Linked list
class CircularLinkedList:
    # Declaring head and tail pointer as null
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    # Creating function for adding new node at the end of the list
    def add(self, data):
        newNode = Node(data)
        # Check whether list is empty
        if self.head.data is None:
            # If list is empty, both head and tail will point to new node
            self.head = newNode
            self.tail = newNode
            newNode.next = s