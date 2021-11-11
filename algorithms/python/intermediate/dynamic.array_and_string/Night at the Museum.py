def min_num_rotations(s):
    pre = 'a'
    min_total = 0
    for c in s:
        # if c > pre:
        #     min_total += min(ord(c) - ord(pre), ord('z') - ord(c) + ord(pre) - ord('a') + 1)
        # else:
        #     min_total += min(ord(pre) - ord(c), ord('z') - ord(pre) + ord(c) - ord('a') + 1)
        distance = abs(ord(c) - ord(pre))
        min_total += distance if distance < 13 else (26 - distance)     
        pre = c
    return min_total


s = input()
print(min_num_rotations(s))
