import sys
sys.setrecursionlimit(1000000)

class node:
	def __init__(self):
		self.isBlock = 0
		self.pre = None
		self.child = dict() 

ans = [] 
for i in range(10002): 
	ans.append("")
s = ""
root = node()

class pair:
	def __init__(self, first, second): 
		self.first = first
		self.second = second
	def __lt__(self, other):
		return self.first < other.first

def add(l, ID):
	tmp = root
	s = ""
	if root.isBlock == 1:
		return False
	for i in range(l):
		check_l = -1
		canmove = False
		for j in range(1, -1, -1):
			if j in tmp.child:
				if tmp.child[j].isBlock == 0:
					if j == 0: 
						s += "0"
					else:
						s += "1"
					tmp = tmp.child[j]
					canmove = True
					break
			else:
				check_l = j
		if canmove == False:
			if check_l == -1:
				return False
			else:
				if check_l == 0:
					s = s + "0"
				else:
					s = s + "1" 
				tmp.child[check_l] = node()
				tmp.child[check_l].pre = tmp
				tmp = tmp.child[check_l]
	tmp.isBlock = 1 
	while tmp != None:
		check = True 
		for j in range(2): 
			if j not in tmp.child: 
				check = False
				
		if check == True:
			if tmp.child[0].isBlock * tmp.child[1].isBlock == 1: 
				tmp.isBlock = 1
		tmp = tmp.pre
	ans[ID] = s
	return True 

n = int(input()) 
a = []
L = list(map(int, input().split(' '))) 

for i in range(n):
	tmp = pair(L[i], i)
	a.append(tmp)
a.sort()
for i in range(n): 
	l = a[i].first
	check = add(l, a[i].second)
	if check == False:
		print("NO")
		sys.exit()

print("YES")
for i in range(n):
	print(ans[i])