class Node:
    def __init__(self):
        self.child = dict()
        self.countWord = 0

def addWord(root, s):
    temp = root
    for ch in list(s):
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.countWord > 0:
            return False
    temp.countWord += 1
    return len(temp.child) == 0

n = int(input())
root = Node()
bad = False
for i in range(n):
    s = input()
    if not addWord(root, s):
        bad = True
        break

if bad:
    print('BAD SET')
    print(s)
else:
    print('GOOD SET')