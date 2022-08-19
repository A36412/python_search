import math

n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def binary_search(a, low, high, so):
    if high > low:
        mid = (high + low) // 2
        if a[mid] == so:
            return mid
        elif a[mid] > so:
            return binary_search(a, low, mid - 1, so)
        else:
            return binary_search(a, mid + 1, high, so)
    else:
        return -1


def exponebtial_search(a, so):
    if not a:
        return -1

    i = 1
    while i < len(a) and a[i] < so:
        i *= 2
    return binary_search(a, i // 2, min(i, len(a) - 1), so)


result = exponebtial_search(a, 5)
if result != -1:
    print("Phan tu o vi tri", result)
else:
    print("Khong tim thay")


