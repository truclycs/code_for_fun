def isPossible(a, n, m):
    s = 1
    sum  = 0
    for i in range(len(a)):
        if a[i] > min:
            return False
        if sum + a[i] > min:
            s += 1
            sum = a[i]
            if s > n:
                return False
        else:
            sum += a[i]
    return True

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        sum = 0
        n = len(A)

        if n < B:
            return -1

        for i in range(n):
            sum += A[i]

        l = 0
        r = sum
        res = 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            if isPossible(A, B, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
