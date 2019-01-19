def intro():
    print("It always maintains a sorted sublist in the lower positions of the list.")


def show():
    print('''
def insertion_sort(A):
   for i in range(1,len(A)): # A[0] sorted
       inserting = A[i]
       while i > 0 and A[i-1] > inserting:
           A[i] = A[i-1]
           A[i-1] = inserting
           i -= 1
   return A
        ''')
