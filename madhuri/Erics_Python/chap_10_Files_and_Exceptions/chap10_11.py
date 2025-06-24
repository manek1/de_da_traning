#10-11. Favorite Number: Write a program that prompts for the user’s favorite
#number. Use json.dump() to store this number in a file. Write a separate program
#that reads in this value and prints the message, “I know your favorite
#number! It’s _____.”

# save_favorite_number.py

import json

filename = 'favorite_number.json'

favorite_number = input("What's your favorite number? ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print("Thanks! I'll remember your favorite number.")
