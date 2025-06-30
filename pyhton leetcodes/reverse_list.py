l = [1,2,3,4]
a = []
i = 0
x = len(l)  # x = 4
while (x>i):   
    a.append(l[x - 1])   # Append the element at position x-1 (starting from the end of list l)   e.g., l[3], l[2], l[1], l[0]
    x = x - 1     # Decrease x to move to the previous element    

print(a)
