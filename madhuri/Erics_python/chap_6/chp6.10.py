#6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
#each person can have more than one favorite number. Then print each person’s
#name along with their favorite numbers.

# Dictionary with people's names as keys and a list of favorite numbers as values
favorite_numbers = {
    'alice': [3, 7, 12],
    'bob': [42, 99],
    'charlie': [5],
    'diana': [9, 10, 11],
    'ethan': [1, 4]
}

# Loop through the dictionary to print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite number(s):")

    # Loop through the list of numbers for each person
    for number in numbers:
        print(f"  - {number}")

    print()  # Blank line for better formatting