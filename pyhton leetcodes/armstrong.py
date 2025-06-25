#  find wether the given number is a armstrong number or not

a = int(input("Enter a number: "))    # the original number
b = 0      # will hold thw sum of cubes of each digits
c = a      # used for comparison with b after the addition process opf cubes

while a > 0:
    d = a % 10      # removes the reamainder eg: 153/10 = 15 remainder = 3
    b += d ** 3     # assigns the remainder to b and cubes it and goes for the 1st iteration  1st: 3x3x3 = 27, 2nd iteration: 27 + 5x5x5x = 152
    a = a//10       # keeps on removing the digit at the unit place eg: 153//10 = 15

if(b == c):         # if addition of cubes = c it is an armstrong number
    print(f"The number {c} is an armstrong")

else:
    print(f"The number {c} is not an armstrong")

