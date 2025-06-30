#  Find the max number in list:

a = [12,45,676,888,999]
max_num = a[0]
for i in a:
    if i > max_num:
        max_num = i

print(f"{max_num} is largest number")

max_num2 = max(a)
print(max_num2)