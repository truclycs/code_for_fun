dict = set()
str = ""
while True:
    try:
        s = input()
        if s != "":
            for x in s.split():
                if x[-1] == '-':
                    hyp = True
                    x = x[:-1]
                for c in x:
                    if c.isalpha():
                        str += c.lower()
                    elif c == '-':
                        str += c
                    else:
                    	str += ' '
                if not hyp:
                    str += ' '
                hyp = False
    except EOFError:
        break
 
for s in str.split():
    dict.add(s)
while len(dict) > 0:
    print(list(sorted(dict))[0])
    dict.remove(list(sorted(dict))[0])  