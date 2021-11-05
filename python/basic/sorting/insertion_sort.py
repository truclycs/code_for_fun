def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while a[j] > tmp and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp


a = [9, 3, 6, 2, 5]
insertion_sort(a)
print(a)
