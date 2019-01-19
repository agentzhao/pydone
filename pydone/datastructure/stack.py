import time
    


def teach():
    print('''Literally a stack of data (like a stack of pancakes)
Additions (push) — always add to the top of the stack
Removals (pop) — always remove from the top of the stack
Pattern type: Last item In is the First item Out (LIFO)
''')

    
    msg = '''Declare the class.
Declare a var for the max num of elements in the stack.
Now the __init__ function.
Declare a list.
Create empty elements in the list with a loop.
Declare the arbitary top position.
Now the is_empty function
Return the '''

    duration = int(input("Pause between lines in sec: "))
    for i in msg.split('\n'):
        print(i)
        time.sleep(duration)
  

def show():
    print('''
class Stack:
    MAX = 100
    def __init__(self):
        self.data = []
        for i in range(self.MAX):
            self.data.append(0)
        self.top = -1
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.MAX - 1
    def push(self, new_data):
        if self.is_full():
            print("Cannot insert to full stack.")
        else:
            self.top += 1
            self.data[self.top] = new_data
    def pop(self):
        if self.is_empty():
            print("Cannot delete from empty stack.")
            return -1
        else:
            result = self.stack[self.top]
            self.top -= 1
            return result
    def peek(self):
        if self.isEmpty():
            print("Empty stack.")
        else:
            return self.data[self.top]
    def display(self):
        if self.isEmpty():
            print("Empty")
        else:
            for i in range(self.top+1): #len of stack
                print(self.data[i])
    ''')
