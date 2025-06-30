l = [1,1,1,2,3,4,5,6,6,7,7,8,9,10]
h = {}
for i in l:
    h[i] = 0
l.clear()
for key in h.keys():
    l.append(key)

print(l)
