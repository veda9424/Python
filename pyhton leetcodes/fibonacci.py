# 1,1,2,3,5,,8,13,..... , n

a = 0
b = 1
temp = 1
num = 10
for i in range(1,num + 1):
    print(f"{temp},",end = " ")
    temp = a+b
    a = b
    b = temp
    