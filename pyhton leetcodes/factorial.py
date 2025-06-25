# 1x2x3x4x5x = 120

def mul(a):
    mul = 1
    for i in range(1, a+1):
        mul = mul * i
    print(mul)

mul(5)