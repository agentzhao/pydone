def intro():
    print("It picks an element as pivot and partitions the given array around the picked pivot.")

def show():
    stype = input("Normal (1) or List Comprehension (2)?")

    if stype == '1':    
        print('''
def quicksort(array):
    if array == []: # terminating condition
        return []
    else:
        pivot = array[0]
        less = []
        great = []
        for i in array[1:]: # from 2nd to last
            if i < pivot:
                less.append(i)
            else:
                great.append(i)
    return quicksort(less) + [pivot] + quicksort(great)
        ''')
    elif stype == '2':
        print('''
def quicksort(elements):
    if len(elements) == 0: # terminating condition
        return []
    else:
        return quicksort([i for i in elements[1:] if i < elements[0]]) + [elements[0]] + quicksort([i for i in elements[1:] if i >= elements[0]])
    ''')
    else:
        print("Input 1 or 2")
