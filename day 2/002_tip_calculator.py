print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
final_result = (bill + bill * (tip/100))/split
print(f"Each person should pay: ${round(final_result,2)}")