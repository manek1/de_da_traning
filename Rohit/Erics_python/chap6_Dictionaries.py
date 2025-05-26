"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary."""
from Rohit.Erics_python.chap5_py import favorite_fruits

person = {"first_name" : "Rohit" ,
          "last_name" : "Sharma" ,
          "age" : "38",
          "city" : "Nagpur"}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program."""
favorite_number = {"Rohit" : 45 ,
                   "Virat" : 18 ,
                   "AB DE" : 17 ,
                   "Surya" : 63 ,
                   "Archer" : 22}
# Printing each person's name and their favorite number
for name, number in favorite_number.items():
    print(f"{name}'s favorite number is {number}.")

"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""
glossary={
    'lists':"Collection of iems accessed from position",
    'dictionary':"Collection of items in key-value form",
    'classes':"Its a blueprint to create objects.  "
}
print("The glossary of items are: ")
for key in glossary:
    print(key+":\n\t"+glossary[key])

"""6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output."""

# Python glossary with 10 terms
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control flow statement for repeating code.',
    'list': 'A collection of ordered items in Python.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list.',
    'string': 'A sequence of characters enclosed in quotes.',
    'integer': 'A whole number, positive or negative, without decimals.',
    'float': 'A number that has a decimal point.',
    'boolean': 'A data type that can be either True or False.'
}

# Loop through the dictionary to print terms and definitions
print("📘 Python Glossary:\n")
for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")

"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary."""
rivers={'Nile':'Egypt','Ganga':'Northern India','Kaveri':'South India'}
for key,value in rivers.items():
    print("\nThe river "+key+" runs through "+value)
print("The list of rivers are: ")
for key in rivers:
    print('\t'+key)
print("The list of countries are: ")
for value in rivers.values():
    print('\t'+value)

"""6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll."""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people_to_take_poll=['jen','max','sarah','edward','pluto']

print('\nThis is solution for 6-6 ')
for people in people_to_take_poll:
    if people in favorite_languages.keys():
        print(people.title()+' has already taken the poll.')
    else:
        print(people.title()+', please take the poll.')

"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person."""
person_1 = {"first_name" : "Rohit" ,
            "last_name" : "Sharma",
            "age" : 38 ,
            "city" : "Nagpur"
            }

person_2 = {"first" : "Virat" ,
            "last_name" : "Kohli" ,
            "age" : 36 ,
            "city" : "Dehli"
            }

person_3 = {"first" : "Francois" ,
            "last_name" : "Plessis" ,
            "age" : 40 ,
            "city" : "Pretoria"
            }
# Store all persons in a list
people = [person_1, person_2, person_3]

# Loop through the list and print details
for person in people:
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")

"""6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet."""
# Define pet dictionaries
pet_1 = {
    'animal': 'dog',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'parrot',
    'owner': 'Ravi'
}

pet_3 = {
    'animal': 'rabbit',
    'owner': 'joe'
}

pet_4 = {
    'animal': 'cat',
    'owner': 'James'
}

# Store all pet dictionaries in a list
pets = [pet_1, pet_2, pet_3, pet_4]

# Loop through the list and print details about each pet
for index, pet in enumerate(pets, start=1):
    print(f"\nPet #{index} Info:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")

"""6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
names to use as keys in the dictionary, and store one to three favorite places 
for each person. To make this exercise a bit more interesting, ask some friends 
to name a few of their favorite places. Loop through the dictionary, and print 
each person’s name and their favorite places"""
favorite_places = {
    'Rohit S': ['Paris', 'Kyoto', 'New York'],
    'SIR Jadeja': ['Bali', 'Goa'],
    'Virat': ['London'],
}
# Dictionary storing people and their favorite places

# Loop through the dictionary
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbersDictionary where each person has a list of favorite numbers
favorite_numbers = {
    'Rohit Sharma': [45, 54, 36],
    'Virat Kohli': [18, 81, 90],
    'AB DE': [17, 71],
    'Surya': [63, 9, 27, 72],
    'Archer': [22, 77]
}

# Loop through the dictionary and print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")

"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it"""
# Dictionary of cities with nested dictionaries for details
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': '37 million',
        'fact': 'Tokyo is the largest metropolitan area in the world.'
    },
    'Paris': {
        'country': 'France',
        'population': '11 million',
        'fact': 'Paris is known as the City of Light.'
    },
    'New York': {
        'country': 'USA',
        'population': '8.5 million',
        'fact': 'New York City is home to the Statue of Liberty.'
    }
}

# Loop through the dictionary and print each city's information
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")

"""6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs 
from this chapter, and extend it by adding new keys and values, changing the context 
of the program or improving the formatting of the output."""
# Function to format and display city information
def display_city_info(city_name, city_info):
    print(f"\n🏙️ City: {city_name}")
    print(f"  🌍 Country: {city_info['country']}")
    print(f"  👥 Population: {city_info['population']}")
    print(f"  🌟 Fact: {city_info['fact']}")
    print(f"  🏞️ Famous Landmark: {city_info['landmark']}")
    print(f"  🧭 Time Zone: {city_info['timezone']}")


# Extended dictionary of cities
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': '37 million',
        'fact': 'Tokyo is the world’s most populous metropolis.',
        'landmark': 'Tokyo Tower',
        'timezone': 'JST (UTC+9)'
    },
    'Paris': {
        'country': 'France',
        'population': '11 million',
        'fact': 'Paris is a global center for art, fashion, and culture.',
        'landmark': 'Eiffel Tower',
        'timezone': 'CET (UTC+1)'
    },
    'New York': {
        'country': 'USA',
        'population': '8.5 million',
        'fact': 'Known as “The Big Apple”.',
        'landmark': 'Statue of Liberty',
        'timezone': 'EST (UTC-5)'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': '20 million',
        'fact': 'Cairo is the largest city in the Arab world.',
        'landmark': 'Pyramids of Giza',
        'timezone': 'EET (UTC+2)'
    }
}

# Print all city information using the function
print("🌐 City Information Explorer:")
for city, info in cities.items():
    display_city_info(city, info)
