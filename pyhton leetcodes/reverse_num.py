num = 1234
i = 0
while num > 0:
    a = num % 10    # 1234 % 10 = 4
    i = i * 10 + a   # 0 * 10 + 4 = 4
    num = num // 10  # 1234 // 10 = 123

print(i)   # i = 4321


