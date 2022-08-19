import math

n = int(input("Nhap so luong phan tu(bang so): "))

a = []
for i in range(0, n):
    a.append(int(input("Nhap phan tu " + str(i + 1) + "(bang so): ")))

def jump_search(a,target,lenght):
    step = int(math.sqrt(lenght))
    last_step = 0
    while a[int(min(step,lenght) -1)] < target:
        last_step = step
        step += math.sqrt(lenght)
        if last_step >= lenght:
            return -1
    while a[int(last_step)] < target:
        last_step +=1
        if last_step == min(step,lenght):
            return -1
    if a[int(last_step)] == target:
        return target
    return -1

result = jump_search(a,3,len(a))

print (str(result))