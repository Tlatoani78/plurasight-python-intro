import random

roll = random.randint(1,6)

guess = int(input(" Guess the dice roll: "))

if guess == roll:
    print("You guessed it right! The dice rolled a " + str(roll) + ". Now go buy yourself a lottery ticket!")
else:
    print("Your guess is incorrect. They dice rolled a " + str(roll) + ".")