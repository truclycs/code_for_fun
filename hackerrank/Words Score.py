if __name__ == '__main__':  
    n = int(input())
    s = input()    
    words = s.split(' ')
    vowels = 'uioaey'    
    res = 0
    for word in words:
        cnt = 0
        for i in range(len(word)):
            if word[i] in vowels:
                cnt += 1
        res += 1 if cnt % 2 else 2                
    print(res)
            