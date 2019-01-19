import time

def intro():
    print('''A tree that branches out up to two nodes at a time.
Root node is the first node.
Leaf nodes are those at the end of the branches.
''')

def teach():
    msg = '''
blah blah blah'''

    duration = int(input("Pause between lines in sec: "))
    for i in msg.split('\n'):
        print(i)
        time.sleep(duration)

def show():
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
