s = input()
t = input()

i = len(s) - 1
while s[i] == 'z':
    i -= 1

s = s[0: i] + chr(ord(s[i]) + 1) + ''.join(['a' for i in range(len(s) - i - 1)])

print(s) if s < t else print('No such string')