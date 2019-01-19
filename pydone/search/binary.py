def intro():
    print("Halving the sorted array for every search.")

def show():
    stype = input("Recursion (1) or Interation (2)?")
    if stype == '1':
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
        return binary_searchr(array, target, mid+1, high)''')
    elif stype == '2':
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
    else:
        print("Input 1 or 2")
