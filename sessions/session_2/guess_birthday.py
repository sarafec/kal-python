day = 0

# prompt the user with the first set
question = "Is your birthday in the first set?\n" + \
            " 1  3  5  7\n" + \
            " 9 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = int(input(question))

if answer == 1:
	day += 1

# prompt the user with the second set
question = "Is your birthday in the second set?\n" + \
            " 2  3  6  7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = int(input(question))

if answer == 1:
	day += 2

# prompt the user with the third set
question = "Is your birthday in the third set?\n" + \
            " 4  5  6  7\n" + \
            "12 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = int(input(question))

if answer == 1:
	day += 4

# prompt the user with the fourth set
question = "Is your birthday in the fourth set?\n" + \
            " 8  9 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = int(input(question))

if answer == 1:
	day += 8

# prompt the user with the fifth set
question = "Is your birthday in the fifth set?\n" + \
            "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = int(input(question))

if answer == 1:
	day += 16

print("\nYour birthday is " + str(day) + "!")