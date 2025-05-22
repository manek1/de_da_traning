#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

# Define the dictionary with personal information

person = {
    'first_name': 'Akshay',
    'last_name': 'Kadam',
    'age': 28,
    'city': 'Solapur'
}

# Print each piece of information
print("First name:", person['first_name'])
print("Last name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])

#----------------------------------------------------------------------------------
#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#Think of five names, and use them as keys in your dictionary. Think of a favorite
#number for each person, and store each as a value in your dictionary. Print
#each person’s name and their favorite number. For even more fun, poll a few
#friends and get some actual data for your program.

# Define the dictionary with favorite numbers

favorite_numbers = {
    'Akshay': 7,
    'Bhairavi': 42,
    'Amit': 3,
    'Aishwarya': 12,
    'Sumit': 5
}

# Print each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

#----------------------------------------------------------------------------------
#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.
#• Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character (\n) to insert a blank line between each word-meaning
#pair in your output.

# We create a dictionary called 'glossary' where:
# - Keys are programming terms (words).
# - Values are their meanings (definitions).

glossary = {
    'variable': 'A named location used to store data in a program.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'An ordered collection of items that can be changed (mutable).'
}

# We use a for loop to go through each word and its meaning.
for word, meaning in glossary.items():
    # Print the word followed by a colon
    print(f"{word}:\n{meaning}\n")

#-----------------------------------------------------------------------------------------
#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

# Define a dictionary called 'glossary' with 10 programming terms and their definitions
glossary = {
    'variable': 'A named location used to store data in a program.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'An ordered collection of items that can be changed (mutable).',
    'tuple': 'An ordered, immutable collection of items.',
    'boolean': 'A data type that can have one of two values: True or False.',
    'if statement': 'A control structure that allows conditional execution of code.',
    'import': 'Used to include external modules or libraries into your program.',
    'comment': 'Text in the code that is ignored by the interpreter, used for notes.'
}

# Loop through the dictionary using a for loop
for word, meaning in glossary.items():
    # Print the word and its meaning, formatted with a newline and indentation
    print(f"{word}:\n  {meaning}\n")

#-----------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------
#6-6. Polling: Use the code in favorite_languages.py (page 104).
#• Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.

# Dictionary: names of people and their favorite programming languages
favorite_languages = {
    'akshay': 'python',
    'bhairavi': 'java',
    'amit': 'c++',
    'aishwarya': 'javascript'
}

# List of people who should take the poll (some are already in the dictionary)
people_to_poll = ['akshay', 'bhairavi', 'sumit', 'anil', 'aishwarya']

# Loop through the list of people to check if they've already taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, we invite you to take the favorite languages poll.")


#-----------------------------------------------------------------------------------------
#6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

# Define three dictionaries representing different people
person1 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

person2 = {
    'first_name': 'Bob',
    'last_name': 'Smith',
    'age': 35,
    'city': 'London'
}

person3 = {
    'first_name': 'Clara',
    'last_name': 'Wang',
    'age': 22,
    'city': 'Beijing'
}

# Store all three people in a list
people = [person1, person2, person3]

# Loop through the list and print information about each person
for person in people:
    # Print each key-value pair in the current person's dictionary
    print("Person Info:")
    for key, value in person.items():
        # Capitalize the key for display
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()  # Add a blank line between people for readability


#-----------------------------------------------------------------------------------------
#6-8. Pets: Make several dictionaries, where the name of each dictionary is the
#name of a pet. In each dictionary, include the kind of animal and the owner’s
#name. Store these dictionaries in a list called pets. Next, loop through your list
#and as you do print everything you know about each pet.

# Create dictionaries for different pets
tommy = {
    'animal': 'dog',
    'owner': 'Alice'
}

mau = {
    'animal': 'cat',
    'owner': 'Bob'
}

nemo = {
    'animal': 'fish',
    'owner': 'Charlie'
}

bella = {
    'animal': 'rabbit',
    'owner': 'Diana'
}

# Store all pet dictionaries in a list
pets = [tommy, mau, nemo, bella]

# Loop through the list and print information about each pet
for pet in pets:
    print("Pet Info:")
    for key, value in pet.items():
        # Print each key-value pair with a neat format
        print(f"  {key.title()}: {value}")
    print()  # Add a blank line between pets


#-----------------------------------------------------------------------------------------
#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.

# Create a dictionary with people's names as keys and lists of favorite places as values
favorite_places = {
    'alice': ['paris', 'tokyo', 'new york'],
    'bob': ['london'],
    'charlie': ['rome', 'barcelona']
}

# Loop through the dictionary to print each person's favorite places
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite place(s):")

    # Loop through the list of places for each person
    for place in places:
        print(f"  - {place.title()}")  # Format each place nicely

    print()  # Add a blank line between entries


#-----------------------------------------------------------------------------------------
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


#-----------------------------------------------------------------------------------------
#6-11. Cities: Make a dictionary called cities. Use the names of three cities as
#keys in your dictionary. Create a dictionary of information about each city and
#include the country that the city is in, its approximate population, and one fact
#about that city. The keys for each city’s dictionary should be something like
#country, population, and fact. Print the name of each city and all of the information
#you have stored about it.

# Main dictionary with cities as keys
cities = {
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'known as the City of Light'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'largest metropolitan area in the world'
    },
    'cairo': {
        'country': 'egypt',
        'population': 9900000,
        'fact': 'home to the Great Pyramids of Giza'
    }
}

# Loop through the cities and print the information
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact'].capitalize()}")


#-----------------------------------------------------------------------------------------
#6-12. Extensions: We’re now working with examples that are complex enough
#that they can be extended in any number of ways. Use one of the example programs
#from this chapter, and extend it by adding new keys and values, changing
#the context of the program or improving the formatting of the output.

# Expanded dictionary with more details per city
cities = {
    'paris': {
        'country': 'france',
        'population': 2148000,
        'fact': 'known as the City of Light',
        'language': 'french',
        'landmark': 'Eiffel Tower'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'largest metropolitan area in the world',
        'language': 'japanese',
        'landmark': 'Tokyo Tower'
    },
    'cairo': {
        'country': 'egypt',
        'population': 9900000,
        'fact': 'home to the Great Pyramids of Giza',
        'language': 'arabic',
        'landmark': 'Great Sphinx'
    },
    'new york': {
        'country': 'usa',
        'population': 8419000,
        'fact': 'nicknamed the Big Apple',
        'language': 'english',
        'landmark': 'Statue of Liberty'
    }
}

# Nicely formatted output
for city, info in cities.items():
    print(f"\n📍 {city.title()}")
    print(f"  🗺️ Country     : {info['country'].title()}")
    print(f"  👥 Population : {info['population']:,}")  # Format number with commas
    print(f"  🌍 Language    : {info['language'].title()}")
    print(f"  🏛️ Landmark    : {info['landmark']}")
    print(f"  📝 Fact        : {info['fact'].capitalize()}")
