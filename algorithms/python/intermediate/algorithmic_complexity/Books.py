n, t = map(int, input().split())
a = list(map(int, input().split()))

num_of_books = 0
total_time = 0
start = 0
for i in range(n):
    total_time += a[i]
    while total_time > t:
        total_time -= a[start]
        start += 1
    num_of_books = max(num_of_books, i - start + 1)
            
print(num_of_books)