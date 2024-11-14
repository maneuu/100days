print("The Love Calculator is calculating your score...")
name1 = input("name: ") # What is your name?
name2 = input("their name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both_name = (name1 + name2).lower()
first_digit = both_name.count("t") + both_name.count("r") + both_name.count("u") + both_name.count("e")
secont_digit =  both_name.count("l") + both_name.count("o") + both_name.count("v") + both_name.count("e")
score = int(str(first_digit) + str(secont_digit))
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")