class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        n = len(A)
        flag = 0
        s = []
        for i in range(n):
            if A[i] == '.' and flag  == 0:
                flag = 1
            elif A[i] == '.' and flag == 1:
                if len(s) != 1:
                    ch = s[-1]
                    while ch != '/':
                        s = s[1:]
                        ch = s[-1]
                flag = 2
            elif A[i] == '/' and flag:
                flag = 0
            else:
                if A[i] == '/' and len(s) == 0:
                    s.append(A[i])
                elif A[i] == '/' and s[-1] == '/':
                    continue
                else:
                    s.append(A[i])

            if s[-1] == '/' and len(s) != 1:
                s = s[1:]

            x = len(s)
            res = ""
            for i in range(x):
                res += s[-1]
                s = s[1:]

            ans = ""
            for i in range(x - 1, -1, -1):
                ans += res[i]

            return ans
                
