#  palindrome means the reverse element is also same eg: markram = markram

a = "markram"
b = a[::-1]    # used for reversing the list
if a == b:
    print("it ia a palindrome")
else:
    print("it is not a palindrome")