rock = """
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

ascii_list = [rock, paper, scissors]

import random

# choices made
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n\t>>>> "))
computer_choice = random.randint(0,2)

# ascii 
if choice > 2 or choice < 0:
  print("You inserted an invalid choice, you lose!")
else:
  print(ascii_list[choice])
  print("\nComputer chose:\n")
  print(ascii_list[computer_choice])
  # result (my handmade code: )
  if choice == computer_choice:
    print("It is a draw")
  elif choice == 0 and computer_choice == 1: # rock -> paper
    print("You lose")
  elif choice == 0 and computer_choice == 2: # rock <- scissors
    print("You won")
  elif choice == 1 and computer_choice == 0: # paper <- rock
    print("You won")
  elif choice == 1 and computer_choice == 2: # paper -> scissors
    print("You lose")
  elif choice == 2 and computer_choice == 0: # scissors -> rock
    print("You lose")
  elif choice == 2 and computer_choice == 1: # scissors <- paper
    print("You won")
  



# result (gpt code)
# if choice == computer_choice:
#         print("It is a draw!")
# elif (choice == 0 and computer_choice == 1) or \
#       (choice == 1 and computer_choice == 2) or \
#       (choice == 2 and computer_choice == 0):
#     print("You lose!")
# else:
#     print("You won!")

