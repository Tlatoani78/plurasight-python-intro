computer_choice = 'scissors'
user_choice = input("Rock, paper, or scissors?: ")
user_choice = user_choice.lower()

if computer_choice == user_choice:
    print("it's a tie!")
elif user_choice == 'rock' and  computer_choice == 'scissors':
    print('you win!')
elif user_choice == 'paper' and  computer_choice == 'rock':
    print('you win!')
elif user_choice == 'scissors' and  computer_choice == 'paper':
    print('you win!')
else:
    print("you lose, computer wins!")