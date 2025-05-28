"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods"""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self .cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The name of my restaurant is "+ self.restaurant_name+". It is famous for its "+ self.cuisine_type )
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open!")

restaurant=Restaurant('RP','Italian')

print("The restaurant named "+restaurant.restaurant_name+ " is gaining much popularity with its "
      "local cuisine popularly referred as : "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""
res1=Restaurant('Panchali','Maharashtrian Cuisine')
res2=Restaurant('Cheese factory','Italian Cuisine')
res3=Restaurant('Xingpo','Chinese Cuisine')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""

class User:
    def __init__(self,first_name,last_name,dob,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender
    def describe_user(self):
        print("The user's name is : "+self.first_name+''+self.last_name +"\n The birthdate is :"+self.dob+'\n The gender is : '+self.gender)
    def greet_user(self):
        print('Hi '+self.first_name+" "+self.last_name+'! It is wonderful to have you on board!')

user1=User('Rohit','Sharma','30/04/1987','M')
user2=User('Virat','Kohli','05/11/1988','M')
user3=User('AB DE','Villiers','17/02/1984','M')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
day of business."""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self .cuisine_type=cuisine_type
        self.number_served = 100
    def describe_restaurant(self):
        print("The name of my restaurant is "+ self.restaurant_name+". It is famous for its "+ self.cuisine_type )
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open!")
    def set_number_served(self,upd_number_served):
        self.number_served=upd_number_served
        print("A total of "+str(self.number_served)+" no of people have been served!")
    def increment_number_served(self,increm_no_of_cust):
        increm_no_of_cust+=self.number_served
        print("The latest incremented no of people served are: "+str(increm_no_of_cust))


restaurant=Restaurant('RP','Italian')

print("The restaurant named "+restaurant.restaurant_name+ " is gaining much popularity with its local cuisine popularly referred as : "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('The restaurant has served a total of '+ str(restaurant.number_served)+' people.')
restaurant.set_number_served(250)
restaurant.increment_number_served(1000)

"""9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0."""
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

user1=User('Rohit','Sharma','30/04/1987','M', 1)
user2=User('Virat','Kohli','05/11/1988','M', 0)
user3=User('AB DE','Villiers','17/02/1984','M', 0)

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self .cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The name of my restaurant is "+ self.restaurant_name+". It is famous for its "+ self.cuisine_type )
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open!")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookie dough']
    def display_flavours(self):
       for i in self.flavours:
            print("The icecream stand has the flavour: "+i+". It is really yum!")

my_ice_cream_stand = IceCreamStand('RP','Dessert')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavours()

"""9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method"""
class User:
    def __init__(self,first_name,last_name,dob,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender
    def describe_user(self):
        print("The user's name is : "+self.first_name+''+self.last_name +"\n The birthdate is :"+self.dob+'\n The gender is : '+self.gender)
    def greet_user(self):
        print('Hi '+self.first_name+" "+self.last_name+'! It is wonderful to have you on board!')

class Admin(User):
    def __init__(self,first_name,last_name,dob,gender):
        super().__init__(first_name,last_name,dob,gender)
        self.privileges=['add post','delete post','ban user']
    def show_privileges(self):
        for i in self.privileges:
            print('The admin can '+i)
a1=Admin('Rohit',' Sharma','30/04/1987','M')
a1.describe_user()
a1.show_privileges()

"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""
class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for i in self.privileges:
            print('This is the method from the Privileges class. The admin can '+i)

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
class Admin(User):
    def __init__(self,first_name,last_name,dob,gender,login_attempts):
        super().__init__(first_name,last_name,dob,gender,login_attempts)
        #Privileges instance as an attribute in the Admin class
        self.privileges=Privileges()
    def show_privileges(self):
        for i in self.privileges:
            print('The admin can '+i)
admin=Admin('Rohit',' Sharma','30/04/1987','M','0')
#admin.describe_user()
#admin.show_privileges()
admin1=Admin('Virat',' Kohli','05/11/1988','M',0)
#admin1.describe_user()
#use your method to show its privileges.
admin1.privileges.show_privileges()

"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range."""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size ==85:
            print("The battery size is already 85")
        else:
            self.battery_size = 85
            print("The battery size has been set to 85")
    def get_range(self):
     #"""Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
            print("The battery of size 70 provides a range of 240")
        elif self.battery_size == 85:
            range = 270
            print("The battery of size 85 provides a range of 270")


    message = "This car can go approximately " + str(range)
    message += " miles on a full charge."
    print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

"""9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
 Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly."""
"""A class representing a restaurant."""

from restourant import Restaurant

channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()

"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that
everything is working correctly."""
from User import Admin

eric = Admin('Rohit', 'Sharma', 'e_ro-hit', 'e_ro-hitexample.com', 'Nagpur')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()

"""9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly."""
from admin_and_privileges import Admin
from admin_and_privileges import Privileges
from User import User
print("#################This is the ouput for the 9-12 ")
a3=Admin('Manoj','Nair','230598','M','10')
a3.priv.show_privileges()