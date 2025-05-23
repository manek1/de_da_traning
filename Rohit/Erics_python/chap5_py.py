"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•	 Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False."""
from tkinter.font import names

car = 'subaru'
color = 'blue'
age = 25
temperature = 30
city = 'New York'

# Tests that evaluate to True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')  # True

print("\nIs age >= 18? I predict True.")
print(age >= 18)  # True

print("\nIs temperature > 20? I predict True.")
print(temperature > 20)  # True

print("\nIs city.lower() == 'new york'? I predict True.")
print(city.lower() == 'new york')  # True

# Tests that evaluate to False
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

print("\nIs color != 'blue'? I predict False.")
print(color != 'blue')  # False

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs temperature == 0? I predict False.")
print(temperature == 0)  # False

print("\nIs city == 'London'? I predict False.")
print(city == 'London')  # False

"""5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:"""
"""""""•	 Tests for equality and inequality with strings"""
name = "Rohit Sharma"
name1 = "rohit sharma"
print("Start")
if name == name1 :
    print("Both the entered names are same")
else:
    print("Both the entered names are NOT same")
print("End")

"""•	 Tests using the lower() function"""
name = "Rohit Sharma"
name1 = "rohit sharma"
print("Start")
if name.lower() == name1 :
    print("Both the entered names are same")
else:
    print("Both the entered names are NOT same")
print("End")
"""•	 Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to"""
age = 21
print("\nIs age == 21? I predict True.")
print(age == 21)  # True

print("\nIs age != 21? I predict False.")
print(age != 21)  # False

print("\nIs age > 18? I predict True.")
print(age > 18)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age >= 21? I predict True.")
print(age >= 21)  # True

print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False

"""•	 Tests using the and keyword and the or keyword"""
marks = 85
attendance = 90

print("\nIs marks > 80 and attendance > 85? I predict True.")
print(marks > 80 and attendance > 85)  # True

print("\nIs marks > 90 and attendance > 85? I predict False.")
print(marks > 90 and attendance > 85)  # False

print("\nIs marks > 90 or attendance > 85? I predict True.")
print(marks > 90 or attendance > 85)  # True

print("\nIs marks < 50 or attendance < 60? I predict False.")
print(marks < 50 or attendance < 60)  # False

"""•	 Test whether an item is in a list"""
colors = ['red', 'blue', 'green']
print("\nIs 'blue' in colors? I predict True.")
print('blue' in colors)  # True

print("\nIs 'purple' in colors? I predict False.")
print('purple' in colors)  # False

"""•	 Test whether an item is not in a list"""
print("\nIs 'yellow' not in colors? I predict True.")
print('yellow' not in colors)  # True

print("\nIs 'green' not in colors? I predict False.")
print('green' not in colors)  # False

"""5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•	 Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
•	 Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
"""
# Alien color is green (this will pass the if test)
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

"""5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
•	 If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
•	 If the alien’s color isn’t green, print a statement that the player just earned
10 points.
•	 Write one version of this program that runs the if block and another that
runs the else block."""
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points.")

"""5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed
for the appropriate color alien."""
alien_color='red'
if alien_color=='green':
    print('The player earns 5 points')
elif alien_color=='yellow':
    print('The player earns 10 points')
elif alien_color=='red':
    print('The player earns 15 points')
else:
    print('No color obtained')

"""5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an
elder."""
age = 45  # You can change this value to test different stages

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

"""5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
•	 Make a list of your three favorite fruits and call it favorite_fruits.
•	 Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!"""
favorite_fruits = ['mango', 'banana', 'apple']

# Checking for specific fruits
if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'grapes' in favorite_fruits:
    print("You really like grapes!")

if 'orange' in favorite_fruits:
    print("You really like oranges!")

"""5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again."""
usernames = ['admin', 'Morris', 'AB DE', 'JP Dumminy', 'J Kalis']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello" +username + " , thank you for logging in again.")

"""5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed."""
user_names=[]
if user_names:
    print('Username sis non empty')
else:
    print('We need to find some users!')

"""5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•	 Make a list of five or more usernames called current_users.
•	 Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•	 Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•	 Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted"""
current_users=['sam','Ash','ram','pam']
current_users=[user.lower() for user in current_users]
new_users=['Bob','Jose','ASH']

for user in new_users:
    if user.lower() in current_users:
        print('Username already used. Try another one!')
    else:
        print('The username can be used')

"""5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line."""
number_list=['1','2','3','4','5','6','7','8','9']

for number in number_list:
    if (number=='1'):
        print('The ordinal number is : '+number+'st!')
    elif (number=='2'):
        print('The ordinal number is : '+number+'nd!')
    elif (number=='3'):
        print('The ordinal number is : '+number+'rd!')
    else:
        print('The ordinal number is : ' + number + 'th!')
