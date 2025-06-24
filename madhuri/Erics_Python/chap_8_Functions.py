#8-1. Message: Write a function called display_message() that prints one sentence
#telling everyone what you are learning about in this chapter. Call the
#function, and make sure the message displays correctly.

def display_message():
    print("In this chapter, I am learning about functions in Python.")

# Call the function
display_message()

#-----------------------------------------------------------------------------------------
#8-2. Favorite Book: Write a function called favorite_book() that accepts one
#parameter, title. The function should print a message, such as One of my
#favorite books is Alice in Wonderland. Call the function, making sure to
#include a book title as an argument in the function call.

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title as the argument
favorite_book("Alice in Wonderland")


#-----------------------------------------------------------------------------------------
#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the
#function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'.")

# Call the function using *positional arguments*
make_shirt("Medium", "Code is life!")

# Call the function using *keyword arguments*
make_shirt(message="Dream Big!", size="Large")


#-----------------------------------------------------------------------------------------
#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
#by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different
#message.

def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a shirt of any size with a custom message
make_shirt(size="Small", message="Keep Calm and Code On")

#-----------------------------------------------------------------------------------------
#8-5. Cities: Write a function called describe_city() that accepts the name of
#a city and its country. The function should print a simple sentence, such as
#Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the
#default country.

def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Call the function with the default country
describe_city("Reykjavik")

# Another city in the default country
describe_city("Akureyri")

# A city in a different country
describe_city("Tokyo", "Japan")


#-----------------------------------------------------------------------------------------
#8-6. City Names: Write a function called city_country() that takes in the name
#of a city and its country. The function should return a string formatted like this:
#"Santiago, Chile"
#Call your function with at least three city-country pairs, and print the value
#that’s returned.

def city_country(city, country):
    return f"{city}, {country}"

# Call the function with three city-country pairs and print the results
location1 = city_country("Santiago", "Chile")
location2 = city_country("Tokyo", "Japan")
location3 = city_country("Paris", "France")

print(location1)
print(location2)
print(location3)

#-----------------------------------------------------------------------------------------
#8-7. Album: Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Add an optional parameter to make_album() that allows you to store the
#number of tracks on an album. If the calling line includes a value for the number
#of tracks, add that value to the album’s dictionary. Make at least one new
#function call that includes the number of tracks on an album.

def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }
    return album

# Create three album dictionaries
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25")
album3 = make_album("Ed Sheeran", "Divide")

# Print the album dictionaries
print(album1)
print(album2)
print(album3)

def make_album(artist, title, tracks=None):
    album = {
        "artist": artist,
        "title": title
    }
    if tracks is not None:
        album["tracks"] = tracks
    return album

# Make album with number of tracks
album4 = make_album("The Weeknd", "After Hours",14)

# Print the new album with tracks
print(album4)

#-----------------------------------------------------------------------------------------
#8-8. User Albums: Start with your program from Exercise 8-7. Write a while
#loop that allows users to enter an album’s artist and title. Once you have that
#information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, tracks=None):
    album = {
        "artist": artist,
        "title": title
    }
    if tracks is not None:
        album["tracks"] = tracks
    return album

print("Enter album information. Type 'quit' at any time to stop.\n")

while True:
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break

    # Optional: ask for number of tracks
    tracks_input = input("Enter number of tracks (or press Enter to skip): ")
    if tracks_input.lower() == 'quit':
        break
    elif tracks_input.isdigit():
        album = make_album(artist, title, int(tracks_input))
    else:
        album = make_album(artist, title)

    print(f"\nAlbum created: {album}\n")

#-----------------------------------------------------------------------------------------
#8-9. Magicians: Make a list of magician’s names. Pass the list to a function
#called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Create a list of magician names
magician_names = ["Houdini", "David Copperfield", "Penn", "Teller"]

# Call the function with the list
show_magicians(magician_names)


#-----------------------------------------------------------------------------------------
#8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
#Write a function called make_great() that modifies the list of magicians by adding
#the phrase the Great to each magician’s name. Call show_magicians() to
#see that the list has actually been modified.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

# Original list of magician names
magician_names = ["Houdini", "David Copperfield", "Penn", "Teller"]

# Modify the list to add "the Great" to each name
make_great(magician_names)

# Show the modified list
show_magicians(magician_names)


#-----------------------------------------------------------------------------------------
#8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
#function make_great() with a copy of the list of magicians’ names. Because the
#original list will be unchanged, return the new list and store it in a separate list.
#Call show_magicians() with each list to show that you have one list of the original
#names and one list with the Great added to each magician’s name.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " the Great")
    return great_magicians

# Original list of magician names
original_magicians = ["Houdini", "David Copperfield", "Penn", "Teller"]

# Call make_great() with a copy of the original list
great_magicians = make_great(original_magicians[:])

# Show both lists
print("Original Magicians:")
show_magicians(original_magicians)

print("\nGreat Magicians:")
show_magicians(great_magicians)

#-----------------------------------------------------------------------------------------
#8-12. Sandwiches: Write a function that accepts a list of items a person wants
#on a sandwich. The function should have one parameter that collects as many
#items as the function call provides, and it should print a summary of the sandwich
#that is being ordered. Call the function three times, using a different number
#of arguments each time.

def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

# Call the function with different numbers of arguments
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")
make_sandwich("avocado", "sprouts", "cucumber", "hummus", "spinach")


#-----------------------------------------------------------------------------------------
#8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
#a profile of yourself by calling build_profile(), using your first and last names
#and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile of yourself
my_profile = build_profile(
    'Alex', 'Smith',
    location='New York',
    field='Software Development',
    hobby='Photography'
)

print(my_profile)

#-----------------------------------------------------------------------------------------
#8-14. Cars: Write a function that stores information about a car in a dictionary.
#The function should always receive a manufacturer and a model name. It
#should then accept an arbitrary number of keyword arguments. Call the function
#with the required information and two other name-value pairs, such as a
#color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was
#stored correctly.

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with required and optional information
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the resulting dictionary
print(car)

#-----------------------------------------------------------------------------------------
#8-15. Printing Models: Put the functions for the example print_models.py in a
#separate file called printing_functions.py. Write an import statement at the top
#of print_models.py, and modify the file to use the imported functions.

# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

# print_models.py

import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

#-----------------------------------------------------------------------------------------
#8-16. Imports: Using a program you wrote that has one function in it, store that
#function in a separate file. Import the function into your main program file, and
#call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *

# greetings.py

def greet_user():
    print("Hello! Welcome to the program.")

# main.py

# 1. import module_name
import greetings
greetings.greet_user()  # Call with module prefix

# 2. from module_name import function_name
from greetings import greet_user
greet_user()  # Call directly

# 3. from module_name import function_name as fn
from greetings import greet_user as gu
gu()  # Call using alias

# 4. import module_name as mn
import greetings as gr
gr.greet_user()  # Call using module alias

# 5. from module_name import *
from greetings import *
greet_user()  # Call directly (not recommended in large projects)


#-----------------------------------------------------------------------------------------
#8-17. Styling Functions: Choose any three programs you wrote for this chapter,
#and make sure they follow the styling guidelines described in this section.

def make_car(manufacturer, model, **car_info):
    """Build a dictionary with information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model

    for key, value in car_info.items():
        car[key] = value

    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


def make_sandwich(*items):
    """Print a summary of the sandwich being made."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!")

make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheese")


def make_album(artist, title, tracks=None):
    """Return a dictionary representing a music album."""
    album = {
        'artist': artist,
        'title': title
    }

    if tracks:
        album['tracks'] = tracks

    return album


album1 = make_album("Adele", "30")
album2 = make_album("Drake", "Scorpion", tracks=25)

print(album1)
print(album2)