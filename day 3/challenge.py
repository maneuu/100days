print('''
⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣏⣀⣀⣀⡀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠙⣿⠉⠛⠛⠛⠛⠲⠶⠶⠶⢦⣤⣤⣤⣤⣰⠏⠀⢹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠹⣇⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⢸⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿⣆⣠⣦⠀⠀⠀⣻⡄⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣵⠶⢶⡴⠖⢶⣄⣤⣾⠁⠿⠋⢿⡤⢶⡟⠈⣷⣸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠀⠀⠀⠀⠈⠀⣿⡀⠀⠀⠀⢀⡾⣥⣤⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣛⣁⣀⠀⢀⣤⠀⠀⠀⠀⠀⠈⠙⠳⠶⠶⠟⠁⢈⣽⠟⣿⣿⣿⣿
⣿⣿⣿⠀⡏⠉⠉⠉⠙⣿⣿⠛⠳⠶⣶⠶⢦⣤⣤⣤⣄⣠⡾⠋⠁⠀⣿⣿⣿⣿
⣿⣿⣿⠀⠹⣄⠀⠀⡸⠇⣿⠐⡶⠀⣿⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⠀⠀⠈⢫⣯⠁⠀⣿⣤⣥⣀⣿⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣀⣴⣿⣿⣿⣿
⣿⣿⣏⠙⢻⣿⣿⣷⣶⣶⣶⣶⣤⣤⣤⣤⣄⣀⣀⣀⣀⣿⣤⡾⠿⢿⣍⣩⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n').lower()
if choice1 == "left":
  print("You've come to a lake. There is an island in the middle of the lake.")
  choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    choice3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
      print('''
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⠀⢀⣶⣿⡛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⢛⣿⣶⡄⠀⣀⠀⠀
⠀⠀⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⠀⠀
⠀⠀⣿⡏⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⢹⣿⠀⠀
⠀⠀⢻⣧⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⣼⡏⠀⠀
⠀⠀⠘⣿⡄⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢰⣿⠃⠀⠀
⠀⠀⠀⠹⣷⡀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢠⣿⡏⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣄⢀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣠⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣿⣾⡿⠋⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⢿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⠟⠀⠀⠀⢹⣿⣿⣿⣿⡏⠀⠀⠀⠻⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ''')
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")