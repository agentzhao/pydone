def teach():
    print("repeatedly swapping the adjacent elements if they are in wrong order")

def show():
    print('''
def bubble_sort(A):
    inorder = False
    while not inorder:
        inorder = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]
                inorder = False
    return A
        ''')
