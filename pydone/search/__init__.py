def help():
    print('linear, binaryr, binaryi, hashtable')

def linear():
    print('''
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
''')

def binaryr():
    print('''
def binary_searchr(array, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_searchr(array, target, low, mid-1)
    else: # target > array[mid]
        return binary_searchr(array, target, mid+1, high)
        ''')

def binaryi():
    print('''
def binary_searchi(array, target):
    low = 0
    high = len(array) -1
    While high:
        mid = (low + high) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
''')

def hashtable():
    print('''
def hashed(element):
    values = []
    for i in element:
        a = ord(i)
        values.append(a)
    value = 0
    for j in values:
        value = value + int(j)
    address = value % 101 + 1
    return address
''')
