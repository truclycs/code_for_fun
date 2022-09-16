class Node:
    def __init__(self):
        self.child = dict()
        self.isLeaf = False

def addWord(root, s):
    flag = False
    temp = root
    for ch in list(s):
        if ch not in temp.child:
            flag = True
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.isLeaf:
            return False
    temp.isLeaf = True
    return flag

n = int(input())
root = Node()
nonVulnerable = True
for i in range(n):
    s = input()
    if not nonVulnerable or not addWord(root, s):
        nonVulnerable = False

if nonVulnerable:
    print("nonvulnerable")
else:
    print("vulnerable")

