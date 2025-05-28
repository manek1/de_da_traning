#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
#a class called IceCreamStand that inherits from the Restaurant class you wrote
#in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
#the class will work; just pick the one you like better. Add an attribute called
#flavors that stores a list of ice cream flavors. Write a method that displays
#these flavors. Create an instance of IceCreamStand, and call this method.

# Parent Class: Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of customers served: {self.number_served}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!\n")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number

    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers

# Subclass: IceCreamStand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"]

    def display_flavors(self):
        print(f"{self.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
        print()  # Add space after the list

# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Frosty Treats")

# Calling the method to display flavors
ice_cream_stand.display_flavors()
