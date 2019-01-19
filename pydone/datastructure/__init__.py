def help():
    print('stack, queue, bst')

def stack():
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

def queue():
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

def singlyll():
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

def doublyll():
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

def bst():
    print('''
class BST:

   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

   def insert(self, data):
       if data < self.data: # insert left
           if self.left is None: # insert as left leaf
               self.left = BST(data)
           else: # recursive left insert
               self.left.insert(data)
       else: # insert right
           if self.right is None: # insert as right leaf
               self.right = BST(data)
           else: # recursive right insert
               self.right.insert(data)

   def search(self, target):
       if self.data == target:
           print("Bingo!")
       elif target < self.data: # go left
           if self.left is None:
               print("Not found.")
           else: # can go left
               self.left.search(target)
       else: # go right
           if self.right is None:
               print("Not found.")
           else: # can go right
               self.right.search(target)
 
   def lookup(self, target, parent=None):# support method to return node, parent
       if self.data == target:
           return self, parent
       elif target < self.data: # go left
           if self.left is None:
               return None, None
           else:
               return self.left.lookup(target, self)
       else: # go right
           if self.right is None:
               return None, None
           else:
               return self.right.lookup(target, self)

   def delete(self, data):
       # get node containing data and its parent
       node, parent = self.lookup(data)
       if node is not None: # data found
           # case 1: node has 0 child, just delete
           if (node.left is None) and (node.right is None):
               # check if it is not the root node
               if parent == None: # whole bst only one entry
                   del node
                   return(“No more BST. :(”)
               elif parent.left is node:
                   parent.left = None
               else:
                   parent.right = None
               del node
           # case 2: node has 1 child, replace node with child
           elif (node.left is None) != (node.right is None):
               if node.left:
                   n = node.left
               else:
                   n = node.right
               if parent is not None:
                   if parent.left is node:
                       parent.left = n
                   else:
                       parent.right = n
               else:
                   if node.left:
                       node.data=node.left.data
                       node.right=node.left.right
                       node.left=node.left.left
                   else:
                       node.data=node.right.data
                       node.right=node.right.right
                       node.left=node.right.left
               del node
           # case 3: node has 2 children, replace with
           # either inorder predecessor or inorder successor
           # we will do inorder successor i.e.
           # smallest value in right subtree
           else:
               parent = node
               successor = node.right
               # find inorder successor
               while successor.left:
                   parent = successor
                   successor = successor.left
               # replace node data by successor data
               node.data = successor.data
               # fix successor's parent node child
               if parent.left == successor: 
                    parent.left = successor.right
               else: # if node.right node has no left node
                    parent.right = successor.right
       else:
           print("Not found.")

   def inorder(self): # Left Root Right 
       if self.left:
           self.left.inorder()
       print(self.data, end=' ')
       if self.right:
           self.right.inorder()

   def preorder(self): # Root Left Right
       print(self.data, end=' ')
       if self.left:
           self.left.preorder()
       if self.right:
           self.right.preorder()

   def postorder(self): # Left Right Root
       if self.left:
           self.left.postorder()
       if self.right:
           self.right.postorder()
       print(self.data, end=' ')

   def reverse(self): # Right Root Left
       if self.right:
           self.right.reverse()
       print(self.data, end=' ')
       if self.left:
           self.left.reverse()

   def smallest(self):
       if self.left is None:
           print("Smallest = ", self.data)
       else:
           self.left.smallest()

   def biggest(self):
       if self.right is None:
           print("Biggest = ", self.data)
       else:
           self.right.biggest()
    ''')
