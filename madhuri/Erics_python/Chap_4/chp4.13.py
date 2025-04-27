#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#simple foods, and store them in a tuple.
#• Use a for loop to print each food the restaurant offers.
#• Try to modify one of the items, and make sure that Python rejects the
#change.
#• The restaurant changes its menu, replacing two of the items with different
#foods. Add a block of code that rewrites the tuple, and then use a for
#loop to print each of the items on the revised menu.

# Initial buffet menu
buffet = ("pasta", "salad", "soup", "bread", "rice")

print("The restaurant offers the following foods:")
for food in buffet:
    print(food)

# Try to modify an item (will cause an error if uncommented)
# buffet[0] = "pizza"  # Tuples are immutable

# Changing the menu (creating a new tuple)
buffet = ("pasta", "salad", "fries", "cake", "rice")

print("\nThe new restaurant menu is:")
for food in buffet:
    print(food)