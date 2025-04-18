'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''
#from pywin.docking.DockingBar import DockingBar


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self .cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The name of my restaurant is "+ self.restaurant_name+". It is famous for its "+ self.cuisine_type )
    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open!")

restaurant=Restaurant('Malabar','Naadan Cuisine')

print("The restaurant named "+restaurant.restaurant_name+ " is gaining much popularity with its local cuisine popularly referred as : "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance.'''

res1=Restaurant('Panchali','Maharashtrian Cuisine')
res2=Restaurant('Cheese factory','Italian Cuisine')
res3=Restaurant('Xingpo','Chinese Cuisine')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()

'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user.'''

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

user1=User('Anjali','Menon','280697','F')
user2=User('Kim','Fox','220198','F')
user3=User('Paul','Christ','230599','M')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

'''9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an 
instance called restaurant from this class. Print the number of customers the 
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number 
of customers that have been served. Call this method with a new number and 
print the value again.

Add a method called increment_number_served() that lets you increment 
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a 
day of business.'''

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


restaurant=Restaurant('Malabar','Naadan Cuisine')

print("The restaurant named "+restaurant.restaurant_name+ " is gaining much popularity with its local cuisine popularly referred as : "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('The restaurant has served a total of '+ str(restaurant.number_served)+' people.')
restaurant.set_number_served(250)
restaurant.increment_number_served(1000)

'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write 
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.'''

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

user1=User('Anjali','Menon','280697','F',1)
#user2=User('Kim','Fox','220198','F')
#user3=User('Paul','Christ','230599','M')

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method.'''

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours='Chocolate'
    def display_flavours(self):
        print("The icecream stand has the flavour: "+self.flavours+". It is really yum!")

amul= IceCreamStand('Amul','Italian')
amul.display_flavours()






