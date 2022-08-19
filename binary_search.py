n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def binary_search(so):
    low = 0
    high = len(a) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if a[mid] == so:
            return mid
        elif a[mid] > so:
            high = mid - 1
        else:
            low = mid + 1
    return None


#
print(binary_search(12))
