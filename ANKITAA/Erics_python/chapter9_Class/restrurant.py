#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
#Make a separate file that imports Restaurant. Make a Restaurant instance,
#and call one of Restaurant’s methods to show that the import statement is working
#properly.

# restaurant.py

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