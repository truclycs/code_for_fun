class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        s = []
        for i in range(len(A)):
            if A[i] == '+' or A[i] == '-' or A[i] == '*' or A[i] == '/':
                a = s[-1]
                s = s[:len(s) - 1]
                b = s[-1]
                s = s[:len(s) - 1]
                if A[i][0] == '+':
                    s.append(a + b)
                elif A[i][0] == '-':
                    s.append(b - a)
                elif A[i][0] == '*':
                    s.append(a * b)
                else:
                    s.append(b // a)
            else:
                s.append(int(A[i]))

        return s[-1]


