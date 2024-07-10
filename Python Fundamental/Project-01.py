import random
print("\n\t------- Snake-Water-Gun Game by Muhammad Bilal Ashiq\n")
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice(s/w/g): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"\n\t--> You chose {reverseDict[you]}\n\t--> Computer chose {reverseDict[computer]}")

if(computer == you):
    print("\n\t==> Its a draw <==")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")


print("\n------------------------- \n")


#  # =========================
# import random
# print("\n\t------- Snake-Water-Gun Game by Muhammad Bilal Ashiq")
# '''
# 1 for snake
# -1 for water 
# 0 for gun
# '''
# computer = random.choice([-1, 0, 1])
# youstr = input("Enter your choice: ")
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# you = youDict[youstr]

# # By now we have 2 numbers (variables), you and computer

# print(f"\n\t--> You chose {reverseDict[you]}\n\t--> Computer chose {reverseDict[computer]}")

# if(computer == you):
#     print("\n\t==> Its a draw <==")

# else:
#     if((computer - you) == -1 or  (computer - you) == 2 ):
#         print("\n\t==> You lose! <==")
#     else:
#         print("\n\t==> You win! <==") 
