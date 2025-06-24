#10-12. Favorite Number Remembered: Combine the two programs from
#Exercise 10-11 into one file. If the number is already stored, report the favorite
#number to the user. If not, prompt for the user’s favorite number and store it in a
#file. Run the program twice to see that it works

import json

filename = 'favorite_number.json'

try:
    # Try to read the number from file
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, ask user and save
    favorite_number = input("I don't know your favorite number yet. What is it? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f"Thanks! I'll remember your favorite number: {favorite_number}.")
else:
    # If the file exists, show the favorite number
    print(f"I know your favorite number! It's {favorite_number}.")
