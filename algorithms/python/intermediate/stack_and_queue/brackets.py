s = input()

brackets = {'(': ')',
            '{': '}',
            '[': ']'}

st = []
valid = True
for c in s:
    if c in brackets.keys():
        st.append(c)
    elif st and brackets[st[-1]] == c:
        st.pop()
    else:
        valid = False
        break

print('valid') if valid and not st else print('invalid')
