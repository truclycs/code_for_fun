dict = set()
while True:
    try:
        s = input().split()
        str = ""
        for x in s:
            for c in x:
                if c.isalpha():
                    str += c.lower()
                else:
                    str += " "
            str += " "
        for s in str.split():
	        dict.add(s)              
    except EOFError:
        break

while len(dict) > 0:
    print(list(sorted(dict))[0])
    dict.remove(list(sorted(dict))[0])    

