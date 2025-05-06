#6-5. Rivers: Make a dictionary containing three major rivers and the country
#each river runs through. One key-value pair might be 'nile': 'egypt'.
#• Use a loop to print a sentence about each river, such as The Nile runs
#through Egypt.
#• Use a loop to print the name of each river included in the dictionary.
#• Use a loop to print the name of each country included in the dictionary.

# Create a dictionary where:
# - The keys are river names.
# - The values are the countries they flow through.

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'ganga': 'india'
}

# Part 1: Print a sentence about each river.
for river, country in rivers.items():
    # Use title() to capitalize the first letter of river and country names.
    print(f"The {river.title()} runs through {country.title()}.")

print()  # Add a blank line for readability

# Part 2: Print the name of each river.
print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

print()  # Add a blank line for readability

# Part 3: Print the name of each country.
print("Countries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")
