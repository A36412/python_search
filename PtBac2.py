import math


def phuong_trinh_bac2():
    a = int(input("Hay Nhap a(bang so): "))
    b = int(input("Hay Nhap b(bang so): "))
    c = int(input("Hay Nhap c(bang so): "))
    if a == 0:
        print("a không được bằng 0")
        a = int(input("Hay Nhap a(bang so): "))
    print("Phuong trinh co dang " + str(a) + "x^2 * " + str(b) + "x *" + str(c))

    Delta = b * b - 4 * a * c
    if Delta == 0:
        print("Phuong trinh co No kep: " + str(-b / (2 * a)))
    elif Delta > 0:
        print("x1 = " + str((-b + math.sqrt(Delta)) / 2 * a) + "x2 = " + str((-b - math.sqrt(Delta)) / 2 * a))
    else:
        print("vo No vi Delta < 0")


phuong_trinh_bac2()
