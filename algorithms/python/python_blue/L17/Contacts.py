class Node:
    def __init__(self, count):
        self.count = count
        self.child = dict()

def addContact(root, s):
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        else:
            root.child[c] = Node(0)
            root = root.child[c]
        root.count += 1        

def countContacts(root, s):    
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        else:
        	return 0
    return root.count

n = int(input())
root = Node(0)
for _ in range(n):
    a, b = input().split()    
    if a[0] == 'a':
        addContact(root, b)
    else:
        print(countContacts(root, b))
