#  MY ATTEMPT

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
index_position = position[0].lower()
if index_position == "a":
  index_position = 0
elif index_position == "b":
  index_position = 1
else:
  index_position = 2
line_position = int(position[1])-1

map[line_position][index_position] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")