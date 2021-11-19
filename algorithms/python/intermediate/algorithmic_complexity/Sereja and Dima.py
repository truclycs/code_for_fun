n = int(input())
a = list(map(int, input().split()))

left = 0
right = n - 1
Sereja = 0
Dima = 0
turn = 0
while left <= right:
    if a[left] > a[right]:
        current = a[left]
        left += 1
    else:
        current = a[right]
        right -= 1
    
    if turn % 2:
        Dima += current
    else:
        Sereja += current
    
    turn += 1

print(Sereja, Dima)