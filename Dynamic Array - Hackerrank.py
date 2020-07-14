import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    res = []
    arr = []
    for i in range(n):
        arr.append([])

    last_ans = 0
    for x in queries:
        index = (int(x[1])^last_ans) % n
        if x[0] == 1:
            arr[index].append(int(x[2]))
        else:
            last_ans = arr[index][int(x[2]) % len(arr[index])]
            res.append(last_ans)

    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()