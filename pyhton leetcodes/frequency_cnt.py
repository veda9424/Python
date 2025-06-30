#  This code is used to count how many times each number appears in a list.

l = [1,1,2,3,4,5,5,5]
h = {}
for i in l:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

for key,values in h.items():
    print(f"{key} has appered {values} times in the list")




from collections import Counter

l = [1,1,1,2,3,4,5,6,6,7,7,8,9,10]
counter = Counter(l)
print(counter)
