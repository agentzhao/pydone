def intro():
    print('''Literally a queue
Additions (enqueue) — always add to the back of the queue
Removals (dequeue) — always remove from the front of the queue
Pattern type: First item In is the First item Out (FIFO)
''')


def teach():
    '''
    blah blah blah
'''

def show():
    print('''
class Queue:

    MAX = 5 # queue can only hold MAX-1 items

    def __init__(self):
        self.data = []
        for i in range(self.MAX):
            self.data.append(0)
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        self.size() == self.MAX -1

    def size(self):
        if self.is_empty():
            return 0
        elif self.front < self.rear:
            return self.rear - self.front
        else: # wrap around
            return self.MAX - self.front + self.rear

    def enqueue(self, value):
        if self.is_full():
            print("Cannot insert to full queue")
        else: # includes wrap around
            self.data[self.rear] = value
            self.rear = (self.rear + 1) % self.MAX

    def dequeue(self):
        if self.is_empty():
            print("Cannot delete from empty queue."
            return -1
        else: # includes wrap around
            result = self.data[self.front]
            self.front = (self.front + 1) % self.MAX
            return result

    def peek(self):
        if self.is_empty():
            print("Empty queue.")
        else:
            return self.data[self.front], self.data[self.rear-1]

    def display(self):
        if self.is_empty():
            print("Empty queue.")
        else:
            if self.front < self.rear: # no wrap around
                for i in range(self.front, self.rear):
                    print(self.data[i])
            else: # wrap around
                for j in range(self.front, self.MAX):
                    print(self.data[j])
                for k in range(0, self.rear):
                    print(self.data[k])
    ''')
