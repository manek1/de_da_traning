#9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
#Add an attribute called number_served with a default value of 0. Create an
#instance called restaurant from this class. Print the number of customers the
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number
#of customers that have been served. Call this method with a new number and
#print the value again.
#Add a method called increment_number_served() that lets you increment
#the number of customers who’ve been served. Call this method with any number
#you like that could represent how many customers were served in, say, a
#day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of customers served: {self.number_served}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Cannot increment by a negative number.")

# Creating the restaurant instance
restaurant = Restaurant("The Spice Garden", "Indian")

# Printing the default number served
print(f"Initial number served: {restaurant.number_served}")

# Changing the value directly
restaurant.number_served = 20
print(f"Updated directly: {restaurant.number_served}")

# Using set_number_served() method
restaurant.set_number_served(50)
print(f"After using set_number_served(): {restaurant.number_served}")

# Using increment_number_served() method
restaurant.increment_number_served(30)
print(f"After incrementing number served: {restaurant.number_served}")
