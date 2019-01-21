def intro():
    print("Every element mapped to a key.")

def show():
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
