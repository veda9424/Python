a = [1,2,3,4]
fir = sec = float('-inf')
for i in a:
    if i > fir:
        sec = fir
        fir = i
    elif fir >= i > sec:
        sec = i

print("sec", sec)
