#•	 Tests for equality and inequality with strings
from numpy.matlib import empty

a1='Ashwathi'
a2='ashwathi'
print('Start')
if a1==a2:
    print('Both the entered names are same')
else:
    print('The entered names are not same')
print('End')

#Tests using the lower() function
a1='Ashwathi'
a2='ashwathi'
print('Start')
if a1.lower()==a2:
    print('Both the entered names are same')
else:
    print('The entered names are not same')
print('End')

#•	 Test whether an item is in a list
items=['bat','ball','cat','rod']
item='bat'
if item in items:
    print('The entered item is present in the list')
else:
    print('The entered item is NOT present in the list')

#•	 Test whether an item is not in a list
item='cow'
if item not in items:
    print('The entered item is NOT present in the list')

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
#variable called alien_color and assign it a value of 'green', 'yellow', or 'red

alien_color=['green','yellow','red']
alien_color='green'
if alien_color=='green':
    print('Bravo!You earned 5 points!' )
else:
    print('No o/p')

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
alien_color=['green','yellow','red']
alien_color='red'
if alien_color=='green':
    print('Bravo!You earned 5 points!' )
else:
    print('Bravo!You earned 10 points!')
#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
#•	 If the alien is green, print a message that the player earned 5 points.
#•	 If the alien is yellow, print a message that the player earned 10 points.
#•	 If the alien is red, print a message that the player earned 15 points.
#•	 Write three versions of this program, making sure each message is printed
#for the appropriate color alien.
alien_color='red'
if alien_color=='green':
    print('The player earns 5 points')
elif alien_color=='yellow':
    print('The player earns 10 points')
elif alien_color=='red':
    print('The player earns 15 points')
else:
    print('No color obtained')
#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
#stage of life. Set a value for the variable age, and then:
#•	 If the person is less than 2 years old, print a message that the person is
#a baby.
#•	 If the person is at least 2 years old but less than 4, print a message that
#the person is a toddler.
#•	 If the person is at least 4 years old but less than 13, print a message that
#the person is a kid.
#•	 If the person is at least 13 years old but less than 20, print a message that
#the person is a teenager.
#•	 If the person is at least 20 years old but less than 65, print a message that
#the person is an adult.
#•	 If the person is age 65 or older, print a message that the person is an
#elder.

age=65
if age<2:
    print('The person is a baby')
elif 2<=age<4:
    print('The person is a toddler')
elif 4<=age<13:
    print('The person is a kid')
elif 13<=age<20:
    print('The person is a teen')
elif 20<=age<65:
    print('The person is an adult')
elif 65 <= age:
    print('The person is an elder')

#5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
#independent if statements that check for certain fruits in your list.
#•	 Make a list of your three favorite fruits and call it favorite_fruits.
#•	 Write five if statements. Each should check whether a certain kind of fruit
#is in your list. If the fruit is in your list, the if block should print a statement,
#such as You really like bananas!

favorite_fruits=['mango','banana','grape']
fruit='kela'
fruit='banana'
#fruit='mango'

if fruit in favorite_fruits:
    if fruit=='banana':
        print("I really like banana!")
    else:
        print('Fruit not the most fav one!')
else:
    print('Fruit not in the list!')

#5-8. Hello Admin: Make a list of five or more usernames, including the name
#'admin'. Imagine you are writing code that will print a greeting to each user
#after they log in to a website. Loop through the list, and print a greeting to
#each user:
#•	 If the username is 'admin', print a special greeting, such as Hello admin,
#would you like to see a status report?
#•	 Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

user_names=['Ash','Sam','admin']
user='Ash'
for user in user_names:
    if user=='admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print('Hello '+user+'.Welcome to our website!')

#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
#not empty.
#•	 If the list is empty, print the message We need to find some users!
#•	 Remove all of the usernames from your list, and make sure the correct
#message is printed.
user_names=[]
if user_names:
    print('Username sis non empty')
else:
    print('We need to find some users!')

#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.
#•	 Make a list of five or more usernames called current_users.
#•	 Make another list of five usernames called new_users. Make sure one or
#two of the new usernames are also in the current_users list.
#•	 Loop through the new_users list to see if each new username has already
#been used. If it has, print a message that the person will need to enter a
#new username. If a username has not been used, print a message saying
#that the username is available.
#•	 Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted.

current_users=['sam','Ash','ram','pam']
current_users=[user.lower() for user in current_users]
new_users=['Bob','Jose','ASH']

for user in new_users:
    if user.lower() in current_users:
        print('Username already used. Try another one!')
    else:
        print('The username can be used')

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
#as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#•	 Store the numbers 1 through 9 in a list.
#•	 Loop through the list.
#•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
#7th 8th 9th", and each result should be on a separate line.

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







