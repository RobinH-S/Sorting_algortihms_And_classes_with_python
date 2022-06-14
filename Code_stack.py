class Stack:
    def __init__(self):
        self.items = [1,2,3,4]

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() <= 0



stack = Stack()
new_list= Stack()

for el in range(new_list.size()):
    new_list.pop()

while 0 < stack.size():
    new_list.push(stack.items[-1])
    stack.pop()

print(new_list.items)


