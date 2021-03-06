stack = []

def empty():
    if len(stack) == 0:
        print('Stack is empty.\n')

    else:
        print(stack, '\n')

val1 = 1
val2 = 2
val3 = 3

stack.append(val1)
stack.append(val2)
stack.append(val3)
empty()

a = stack.pop()
b = stack.pop()
c = stack.pop()

print('The popped elements are : ', a, b, c, '\n')
empty()


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()

while True:
    print('1. Push')
    print('2. Push')
    print('3. Push')

    do = int(input('What would you like to do?:'))

    if do == 1:
        val = input('Enter the value: ')
        s.push(val)

    elif do == 2:
        if s.is_empty():
            print('Stack is empty\n')

    elif do == 3:
        break