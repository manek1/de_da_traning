#7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
#the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has
#run out of pastrami, and then use a while loop to remove all occurrences of
#'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
#in finished_sandwiches.

# Initial sandwich orders with 'pastrami' appearing 3 times
sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "veggie", "pastrami", "beef"]
finished_sandwiches = []

# Notify that pastrami is unavailable
print("Sorry, the deli has run out of pastrami.\n")

# Remove all 'pastrami' from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a summary of finished sandwiches
print("\nAll the sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.capitalize()} sandwich")