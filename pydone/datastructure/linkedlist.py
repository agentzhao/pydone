
def intro():
    ltype = input("Singly (1) Doubly (2) or Circular(3) Linked List?")
    if ltype == '1':
        print('''A list nodes that are linked together.
Additions (enqueue) — always add to the back of the queue
Removals (dequeue) — always remove from the front of the queue
Pattern type: First item In is the First item Out (FIFO)
''')


def show():
    ltype = input("Singly (1) Doubly (2) or Circular(3) Linked List? ")
    if ltype == '1':
        show_singlyll()
    elif ltype == '2':
        show_doublyll()
    elif ltype == '3':
        show_circularll()
    else:
        print("Type 1, 2 or 3.")

def show_singlyll():
    print('''
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None
        #self.length = 0
        
    def insert(self, newdata):
        newnode = Node(newdata)
        #self.length += 1
        curr = self.head
        prev = None
        while curr and curr.data < newdata:
            prev = curr
            curr = curr.link
        newnode.link = curr
        if prev is None:
            self.head = newnode
        else:
            prev.link = newnode

    def delete(self, target):
        curr = self.head
        prev = None
        while curr and curr.data < target:
            prev = curr
            curr = curr.link
        if curr.data != target:
            print('not found')
        elif prev is None:
            self.head = curr.link
        else:
            prev.link = curr.link

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.link
        print()
''')

def show_doublyll():
    print('''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        #self.length = 0

    def insert(self, newdata):
        newnode = Node(newdata)
        #self.length += 1
        if self.head is None: # empty list
            self.head = newnode
            self.tail = newnode
        else:
            curr = self.head
            while curr and curr.data < newdata:
                curr = curr.next
            if curr == self.head: # insert start
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif curr is None: # insert end
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else: # in between
                newnode.prev = curr.prev
                newnode.next = curr
                curr.prev.next = newnode
                curr.prev = newnode

    def delete(self, target):
        if self.head == None: # empty
            print("empty")
        else:
            curr = self.head
            while curr and curr.data < target:
                curr = curr.next
            if curr.data == target: # found
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                del curr
            else:
                print("not found")

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()
''')

def show_circularll():
    print('''
class Circular_Queue:
    def init(self, maxsize):
        self.queue = [None for i in range(size)]
        self.front = None
        self.rear = None
        self.maxsize = maxsize

    def findSize(self):
        if self.front == None:
            return 0
        if self.front < self.rear:
            return self.rear - self.front
        else:
            return self.rear + self.maxsize - self.front

    def isEmpty(self):
        return self.front == None

    def isFull(self):
        return self.findSize() == self.maxsize - 1

    def enqueue(self, data):
        if self.isFull():
            print('Cannot insert to full queue.')
            return False
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.maxsize

    def dequeue(self):
        if self.isEmpty():
            print('The queue is empty')
            return False
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return data

    def peek(self):
        if self.isEmpty():
            print('The queue is empty')
            return False
        else:
            return self.queue[self.front]

    def display(self):
        start = self.front
        while start != self.rear:
            print(self.queue[start], end = ' ')
            start = (start + 1) % self.maxsize
        print()
''')
