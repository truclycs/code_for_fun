def deleteSign(s):
    res = ""
    for x in s:
        if x.isalpha():
            x = x.upper()
            res += x
    return res

a = input()
b = input()
c = input()
n = int(input())
a = deleteSign(a)
b = deleteSign(b)
c = deleteSign(c)
abc = a + b + c
acb = a + c + b
bac = b + a + c
bca = b + c + a
cab = c + a + b
cba = c + b + a
for i in range(n):
    s = input()
    s = deleteSign(s)
    if s == abc or s == acb or s == bac or s == bca or s == cab or s == cba:
        print("ACC")
    else:
        print("WA")
