#Function multiply_it() multiplies all numbers in the list and prints result
def multiply_it(tuple): #tar inn en tuple og iterer igjennom alle elementene og ganger hvert element med total variabelen
    total = 1
    for number in tuple:
        total *= number
    print(total)

my_tuple = (3, 6 , 12 , 24, 48,)
multiply_it(my_tuple)



#Reverse list with stack
class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() <= 0


eks = [1,2,3,4,35, 54, 23, 111, 5000000]

#Creating an instance of Stack, so the methods of stack can be called on the object
stack = Stack()
new_list = Stack()

#appending example list to the stack.items list
stack.items.append(eks)



def reverse_list(items):
    while 0 < stack.size():
        new_list.push(stack.items[0])
        stack.pop()
    print(new_list.items)

#Calling reverse_list function on new_list.items
reverse_list(new_list.items)
