def intro():
    print("Looping through the array one after another")

def show():
    print('''
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
''')
