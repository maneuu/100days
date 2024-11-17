target = int(input("Insert a value to sum all the even numbers between 1 and your value:\n\t >>>>")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
if target >=0 and target <= 1000:
  for even in range(1,target + 1):
    if even % 2 == 0:
      total+= even
print(total)