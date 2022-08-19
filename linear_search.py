n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))


def linear_search():
    x = int(input("Hay nhap so ban can tim(bang so): "))
    for i in range(len(a)):
        if x == a[i]:
            return print("Phan tu ban can tim nam o vi tri " + str(i))
    return print("Khong co")


linear_search()

