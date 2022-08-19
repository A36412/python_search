n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def termary_search(low, high, so):
    if high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if a[mid1] == so:
            return mid1
        elif a[mid2] == so:
            return mid2
        elif a[mid1] > so:
            return termary_search(low, mid1 - 1, so)
        elif a[mid2] > so:
            return termary_search(mid2 + 1, high, so)
        else:
            return termary_search(mid1 + 1, mid2 - 1, so)
    return -1


so = 10
result = termary_search(0, len(a), so)

if result != -1:
    print("Phan tu o vi tri", result + 1)
else:
    print("Khong tim thay")
