n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def selection_sort():
    min = 0
    for i in range(0, len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if (a[j] < a[min]):
                min = j
        if (min != i):
            a[min], a[i] = a[i], a[min]
    print(a)


selection_sort()
