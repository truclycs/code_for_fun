def repeatedNumber(self, A):
    res = []
    n = len(A)
    d = [0] * (n + 2)
        
    for i in range(n):
        if d[A[i]] == 1:
            res.append(A[i])  
        d[A[i]] = 1
            
    for i in range(1, n + 1):
        if not d[i]:
            res.append(i)   
            break       
    return res