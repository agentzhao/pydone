def intro():
    print("Halving the sorted array for every search.")

def show():
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
    
