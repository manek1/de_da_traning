class User:
    def __init__(self,first_name,last_name,dob,gender,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender
        self.login_attempts=login_attempts

    def describe_user(self):
        print("The user's name is : "+self.first_name+''+self.last_name +"\n The birthdate is :"+self.dob+'\n The gender is : '+self.gender)
    def greet_user(self):
        print('Hi '+self.first_name+" "+self.last_name+'! It is wonderful to have you on board!')
    def increment_login_attempts(self):
        incremented_value_of_login_attempt=self.login_attempts+1
        print("The incremented value of login attempts is :"+str(incremented_value_of_login_attempt))
    def reset_login_attempts(self):
        login_attempts=0
        print("The login attempt have been reset to 0")

class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for i in self.privileges:
            print('This is the method from the Privileges class. The admin can '+i)

class Admin(User):
    def __init__(self,first_name,last_name,dob,gender,login_attempts):
        super().__init__(first_name,last_name,dob,gender,login_attempts)
        #Privileges instance as an attribute in the Admin class
        self.priv=Privileges()
    '''def show_privileges(self):
        for i in self.privileges:
            print('The admin can '+i)'''

a1=Admin('Rohit','Sharma','30/04/1987','F','4')
a1.priv.show_privileges()

"""9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary."""
glossary = {
    'variable': 'A storage location paired with an associated symbolic name.',
    'function': 'A block of organized, reusable code used to perform a single action.',
    'loop': 'A programming structure that repeats a sequence of instructions.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'
}

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")

from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'A storage location paired with an associated symbolic name.'
glossary['function'] = 'A block of organized, reusable code used to perform a single action.'
glossary['loop'] = 'A programming structure that repeats a sequence of instructions.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['dictionary'] = 'A collection of key-value pairs.'

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")

"""9-14. Dice: The module random contains functions that generate random numbers in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times."""

from random import randint

class Die:
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)
