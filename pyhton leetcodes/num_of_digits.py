# Write a program to count the number of digits in a given integer.

num = 1234
cnt = 0
while num != 0:   # loop will go on until the num = 0
    num = num // 10     # 1234 // 10 = 123, 123 // 10 = 12
    cnt += 1            # count keeps on increasing by 1

print(cnt)      # when the loop ends the total count will be 4