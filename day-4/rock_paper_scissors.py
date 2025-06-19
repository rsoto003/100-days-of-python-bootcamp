import random
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = ['Rock', 'Paper', 'Scissors']
game = []
user_choice = input('Rock, paper, or scissors, Shoot! \n> ').capitalize()
computer_choice = random.choice(choices)

game.extend([user_choice, computer_choice])

if 'Rock' in game and 'Paper' in game:
    if computer_choice == 'Paper':
        print('The computer wins!')
    else:
        print('You win!')
elif 'Rock' in game and 'Scissors' in game:
    if computer_choice == 'Rock':
        print('The computer wins!')
    else:
        print('You win!')
elif 'Scissors' in game and 'Paper' in game:
    if computer_choice == 'Scissors':
        print('The computer wins!')
    else:
        print('You win!')
elif computer_choice == user_choice:
    print('Draw!')
else:
    print('I think you may have missed reading the instructions. Please try again! :)')

print(f'The computer chose {computer_choice}')
print(f'The user chose {user_choice}')




