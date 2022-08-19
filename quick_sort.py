n = int(input("Nhap so luong phan tu(bang so): "))

a = []

for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def quick_sort(a, left, right):
    i = left
    j = right
    pivot = a[left]
    while (i <= j):
        while a[i] < pivot and i < right:
            i += 1
        while a[j] > pivot and j > left:
            j -= 1
        if (i <= j):
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if (left < j):
        quick_sort(a, left, j)
    if (i < right):
        quick_sort(a, i, right)


quick_sort(a, 0, n - 1)
print(a)
