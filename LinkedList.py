class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None  # head is the first node here
        self.size = 0

    # inserting a node at the start
    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)  # object of node class

        if not self.head:
            self.head = newNode  # if head is null then it will be the first node
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size1(self):
        return self.size  # for linkedlist size

    # inserting node at the end
    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)  # instantiating the Node class
        actualNode = self.head  # Marking the first node with a pointer

        # traversing to the last node
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode  # updating the pointer

    # Traversing the list
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    # for removing node
    def remove(self, data):
        if self.head is None:
            return
        self.size = self.size - 1
        currentNode = self.head  # pointers for prev. and next node
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


# Testing linkedlist operations
linkedlist = LinkedList()  # object of LinkedList class

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertStart(31)

linkedlist.traverseList()

print(linkedlist.size1())

linkedlist.remove(31)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)

print(linkedlist.size1())
