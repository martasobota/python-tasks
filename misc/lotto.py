#Simulator of lotto game (6 numbers from 1 to 49 👍)

import random

random_six = random.sample(range(1,49), 6)
# print(random_six)
user_nums = []


print ("Pass six chosen numbers from 1 to 49 and become a millioner! 💸 ")
user_nums = []
while len(user_nums) < 6:
    print ("Choice number: {}".format(len(user_nums) + 1))
    try:
        i = int(input("Pass your number here --> "))
        if (i not in user_nums) and (1 <= i <= 49) and type(i) == int:
            user_nums.append(i)
    except:
        print ("Pass N-U-M-B-E-R-S!)")
        
user_nums.sort()

user_chosen_numbers = ', '.join([str(i) for i in user_nums])

print("Your numbers are: " + str(user_chosen_numbers))

check1 = set(user_nums)
check2 = set(random_six)

final_check = check1.intersection(check2)

variable = len(final_check)

if variable == 1:
    print("You hit 1 number. Lucky numbers were: {}".format(', '.join([str(i) for i in random_six])))
elif variable == 2:
    print("You hit 2 numbers. Lucky numbers were: {}".format(', '.join([str(i) for i in random_six])))
elif variable == 3:
    print("Wow! You got 3!")
elif variable == 4:
    print("Wow! You got 4! 💰")
elif variable == 5:
    print("Lucky you! You hit 5 numbers! 💵")
elif variable == 6:
    print("Whoa! You hit all 6 numbers!!! 💸")
else:
    print("No lucky choices, maybe next time! Lucky numbers were: {}".format(', '.join([str(i) for i in random_six])))

