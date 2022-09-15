class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        cnt = 0
        cntSign = 0
        tmp = 0
        for i in range(len(A)):
            if A[i] == '(':
                cnt += 1
                tmp += 1
            if A[i] == ')':
                cnt -= 1
            if A[i] == '+' or A[i] == '-' or A[i] == '*' or A[i] == '/':
                cntSign += 1

            if cnt == 0:
                if tmp > cntSign:
                    return 1
                else:
                    tmp = 0
                    cntSign = 0 
        return 0
           

