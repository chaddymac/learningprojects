import random
import sys

# Range arguments/ Choice of the parameters you enter for the game.
arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

# Generating a random number
random_num = random.randint(arg1, arg2)

# Taking the users guess
guess = int(input("guess a number "))


# While loop which allows the player to keep guessing a number
while guess != random_num:
    print("nope try again")
    guess = int(input("guess a number "))
print("you got it")
