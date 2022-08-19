class Myprint:
    def __init__(self, fstring):
        self.fistString = fstring

    def string_to_print(self):
        # self.fistString = input()
        print("chuoi ban vua nhap: "+ self.fistString)

    def string_to_upper(self):
        print("chuoi ban vua nhap nhung viet hoa: " + self.fistString.upper())


x = input("Hay nhap chuoi ma ban muon: ")
p1 = Myprint(x)
print(p1.string_to_print())
print(p1.string_to_upper())
