def cnt_char(s):
    char = [0] * 26
    for c in s:
        char[ord(c) - ord('a')] += 1
    return char


def check_type(s, t):
    char_s = cnt_char(s)
    char_t = cnt_char(t)

    for i in range(26):
        if char_t[i] > char_s[i]:
            return "need tree"

    if len(t) == len(s):
        return "array"  # only need shuffle position from s

    j = 0
    for i in range(len(s)):
        if s[i] == t[j]:
            j += 1
            if j == len(t):
                return "automaton"  # only need delete any position to change from s to t
    return "both"


s = input()
t = input()
print(check_type(s, t))