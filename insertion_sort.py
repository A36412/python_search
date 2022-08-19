n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def insertion_sort():
    pos = 0
    x = 0
    for i in range(1, len(a)):
        x = a[i]
        pos = i
        while pos > 0 and x < a[pos - 1]:
            a[pos] = a[pos - 1]
            pos -= 1
        a[pos] = x
    print(a)


insertion_sort()
