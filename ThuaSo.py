n = int(input("Nhap phan tu muon phan ra thanh thua so (Bang So): "))


def so_nguyen(n):
    i = 2
    list_so = []
    while (n > 1):
        if n % i == 0:
            n = (int(n / i))
            list_so.append(i)
        else:
            i = i + 1
    if len(list_so) == 0:
        list_so.append(n)
    return list_so


list_so = so_nguyen(n)
size = len(list_so)
sb = " "
for i in range(0, size - 1):
    sb = sb + str(list_so[i]) + "x"
sb = sb + str(list_so[size - 1])
print(n, "=", sb)
