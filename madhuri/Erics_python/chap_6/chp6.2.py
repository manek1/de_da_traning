#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.

# Define the dictionary with favorite numbers

favorite_numbers = {
    'Nisha': 7,
    'Shyam': 42,
    'Amit': 3,
    'Amar': 12,
    'Sumit': 5
}

# Print each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")