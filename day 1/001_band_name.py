#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Greetings, traveler! Let's create an awesome band name together! Just share the name of your city and your pet below.\n")

city = input("What's the name of the city where you were born?\n\t")

pet_name = input("And your pet's name?\n\t")

band_name = f"{city} {pet_name}"
print(f"How about 'The {band_name} Band'?")
