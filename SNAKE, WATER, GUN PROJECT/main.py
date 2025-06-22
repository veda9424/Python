'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter Your Choice between Snake,Gun,Water: ")
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]    # assign the value as per the user input if s then you will be 1

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("Its a Draw")

else:
    if(computer == -1 and you == 1):
        print("You Win")

    elif(computer == 1 and you == -1):
        print("You Loose")

    elif(computer == -1 and you == 0):
        print("You Loose")

    elif(computer == 0 and you == -1):
        print("You Win")

    elif(computer == 1 and you == 0):
        print("You Win")

    elif(computer == 0 and you == 1):
        print("You Win")

    else:
        print("something went wrong")

