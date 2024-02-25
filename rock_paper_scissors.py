import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Rock, paper, or scissors?: ")
user_choice = user_choice.lower()

if computer_choice == user_choice:
    print("it's a tie! the computer chose " + computer_choice + ".")
elif user_choice == 'rock' and  computer_choice == 'scissors':
    print("you win! the computer chose " + computer_choice + ".")
elif user_choice == 'paper' and  computer_choice == 'rock':
    print("you win! the computer chose " + computer_choice + ".")
elif user_choice == 'scissors' and  computer_choice == 'paper':
    print("you win! the computer chose " + computer_choice + ".")
else:
    print("you lose, computer wins! the computer chose " + computer_choice + ".")