#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
#different instances from the class, and call describe_restaurant() for each
#instance.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}\n")

# Creating three different restaurant instances
restaurant1 = Restaurant("The Spice Garden", "Indian")
restaurant2 = Restaurant("Pasta Paradise", "Italian")
restaurant3 = Restaurant("Sushi World", "Japanese")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
