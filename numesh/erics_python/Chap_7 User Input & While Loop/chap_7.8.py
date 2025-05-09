#7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
#sandwiches. Then make an empty list called finished_sandwiches. Loop
#through the list of sandwich orders and print a message for each order, such
#as I made your tuna sandwich. As each sandwich is made, move it to the list
#of finished sandwiches. After all the sandwiches have been made, print a
#message listing each sandwich that was made.

# List of sandwich orders
sandwich_orders = ["tuna", "chicken", "pastrami", "veggie", "beef"]

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Process each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich in the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print all finished sandwiches
print("\nAll the sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.capitalize()} sandwich")
