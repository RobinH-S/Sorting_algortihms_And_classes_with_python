class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node


    def getData(self):
        return data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.next_node

    def setNextNode (self, val):
        self.next_node = val



class LinkedList:

    def __init__(self, head= None):
        self.head = head
        self.size = 0


    def getHead(self):
        return self.head

    def setHead (self, val):
        self.head = val

    def getSize(self):
        return self.size

    def setSize(self, val):
        self.size = val


    def addNode(self, data):
        new_node = Node (data, self.head)
        self.head = new_node
        self.size +=1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()



my_link = LinkedList ()

my_link.addNode ('HEllo')
my_link.addNode('in')
my_link.addNode ('reverse')

my_link.printNode()
