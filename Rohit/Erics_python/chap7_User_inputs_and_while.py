"""7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”"""

rental_car = input("What kind of rental car would you like?")
print("Let me see if I can find you a " + rental_car + ".")

"""7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying 
they’ll have to wait for a table. Otherwise, report that their table is ready"""
people = input("How many people are in your dinner group?")
people = int(people)
if people > 8 :
    print("You'll hsve wait for a table.")
else :
    print("Your table is ready")

"""7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not."""
# 7-3: Multiples of Ten

# Ask the user for a number
number = input("Please enter a number: ")

# Convert the input to an integer
number = int(number)

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

"""7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza."""
pizza = "Please enter your choice of topping: "
pizza+="\n Enter 'quit' when you are finished."
while True:
    topping=input(pizza)
    if topping=='quit':
        break
    else:
        print("I will add the topping :"+topping+" to your Pizza!")

"""7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket."""
pizza="Enter your age and I shall tell the movie fare. "
pizza+="\nEnter 'quit' to exit."

while True:
    person_age=input(pizza)

    if (pizza=='quit'):
        break
    elif (int(person_age)<3):
        print("Your age is less than 3 so the ticket is free.")
    elif (3<=int(person_age)<=12):
        print("Your age is in the range 3-12, so the ticket price  is 10.")
    elif (12<int(person_age)):
        print("Your age is greater than 12,so the ticket price  is 15.")

"""7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value."""
age_input = ""  # Initial value

while age_input != 'quit':
    age_input = input("Enter your age (or type 'quit' to exit): ")

    if age_input == 'quit':
        print("Goodbye!")
    else:
        age = int(age_input)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")


"""7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)"""
while True:
    print("This loop will run forever! Press Ctrl+C to stop it.")

"""7-8. Deli: Make a list called sandwich_orders and fill it with the names of 
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made."""
# List of sandwich orders
sandwich_orders = ['tuna', 'turkey', 'pastrami', 'chicken', 'veggie']

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Making each sandwich
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first sandwich from the list
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Printing all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")

"""7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""
# Step 1: List with 'pastrami' at least 3 times
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'chicken', 'veggie', 'pastrami']

# Step 2: Empty list for finished sandwiches
finished_sandwiches = []

# Step 3: Print deli warning
print("Sorry, the deli has run out of pastrami.\n")

# Step 4: Remove all 'pastrami' sandwiches from the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Step 5: Make remaining sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Step 6: Final message
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")

"""7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll."""
# Create an empty dictionary to store responses
responses = {}

# Flag to indicate if polling is active
polling_active = True

while polling_active:
    # Ask for the person's name and their dream vacation
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    responses[name] = place

    # Ask if another person wants to respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

# Polling is complete, print the results
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
