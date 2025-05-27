"""8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly"""
def display_message():
    """Display a message about what you're learning."""
    print("In this chapter, I'm learning about functions in Python!")

# Call the function
display_message()

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""
def favorite_book(title):
    """Displays the fav book"""
    print("One of my fav books is: "+title)

# Call the function with a book title
favorite_book("Alice in Wonderland")

"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments."""
def make_shirt(size,text_msg):
    """function used to print a sentence summarizing the size of the shirt and the message printed on it"""
    print(" A shirt of size "+size+" is printed with the text message as "+text_msg)

make_shirt('large' ,'Python is Awesome!')

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""
def make_shirt(size='large',text_msg='I love Python'):
    print(" A shirt of size " + size + " is printed with the text message as " + text_msg)
make_shirt()
make_shirt('medium')
make_shirt('38','Code More, Worry Less')

"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country"""
def describe_city(city,country='USA'):
    print("The city "+city+" is in the country "+country)

# Call the function for three different cities
describe_city("New York")          # Uses default country
describe_city("los angeles")       # Uses default country
describe_city("tokyo", "japan")    # Specifies a different country

"""8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned."""
def city_country(city,country):
    """Function to return formatted string 'city, country'"""
    formatted_string =print('"'+city+','+country+'"')
    return formatted_string

city_country('Mumbai','India')
city_country('Paris','France')
city_country('New York','USA')

"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album"""
def make_album(artist_name,album_title,number_of_tracks=''):
    """Return a dict of muisc album"""
    music_album={'artist':artist_name,'title':album_title}
    if number_of_tracks :
        music_album['track']=number_of_tracks
    return music_album

album1=make_album('Atif','Unplugged')
album2=make_album('Arijit','Melody')
album3=make_album('Lataji','Old','1000')
print(album1)
print(album2)
print(album3)

"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""
while True:
    artist_name = input("Enter artis's name = ")
    print("Enter q anytime to quit")
    if artist_name=='q':
        break
    album_title=input("Enter album's title = ")
    print("Enter q anytime to quit")
    if album_title=='q':
        break
    number_of_tracks=input("Enter the number of tracks = ")
    print("Enter q anytime to quit")
    if number_of_tracks=='q':
        break
    #music_album=make_album('artist_name':artist_name,'album_title':album_title,'track_record':number_of_tracks)
    music_album = make_album(artist_name, album_title,number_of_tracks)
    print(music_album)

    """8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list"""
# List of magician names
magician_names = ['houdini', 'david copperfield', 'criss angel', 'dynamo']
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print("The name of the magicians is :" +magician.title())

# Call the function with the list
show_magicians(magician_names)

"""8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified."""
magician_names = ['houdini', 'david copperfield', 'criss angel', 'dynamo']
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print("The name of the magicians is :" +magician.title())
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i]='The Great '+magicians[i]
        #return magicians

make_great(magician_names)
show_magicians(magician_names)

"""8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
 names and one list with the Great added to each magician’s name."""
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Return a new list with 'the Great' added to each magician's name."""
    great_magicians = []
    for magician in magicians:
        great_magicians.append(magician + " the Great")
    return great_magicians

# Original list of magician names
magician_names = ['Houdini', 'David Copperfield', 'Criss Angel', 'Dynamo']

# Create a new list with "the Great" added
great_magicians = make_great(magician_names[:])  # Use a copy of the original list

# Show the original list (unchanged)
print("Original Magicians:")
show_magicians(magician_names)

# Show the modified list
print("\nGreat Magicians:")
show_magicians(great_magicians)

"""8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that
is being ordered. Call the function three times, using a different number of arguments each time."""
def sandwich_topping(*toppings):
    print("The sandwich has below toppings : \n\t"+str(toppings))

sandwich_topping('turkey', 'lettuce', 'tomato')
sandwich_topping('chicken', 'mayo')
sandwich_topping('avocado', 'bacon', 'egg', 'cheese', 'spinach')

"""8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you."""
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
        return profile

user_profile = build_profile('Rohit', 'Sharma', location='Nagpur', field='indian Cricker')
my_call=build_profile('Viat','Kohli',job='BCCI',native_place='Mumbai')
print(user_profile)
print(my_call)

"""8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly"""
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the returned dictionary
print(car)

