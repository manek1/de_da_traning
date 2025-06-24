#7-1. Rental Car: Write a program that asks the user what kind of rental car they
#would like. Print a message about that car, such as “Let me see if I can find you
#a Subaru.”

# Ask the user what kind of rental car they would like
car_type = input("What kind of rental car would you like? ")

# Print a message about that car
print(f"Let me see if I can find you a {car_type.title()}.")

#-----------------------------------------------------------------------------------------
#7-2. Restaurant Seating: Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message saying
#they’ll have to wait for a table. Otherwise, report that their table is ready.

hotel_dinner=int(input("how many people are in their dinner group?"))
print(hotel_dinner)
if hotel_dinner>8 :
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

#-----------------------------------------------------------------------------------------
#7-3. Multiples of Ten: Ask the user for a number, and then report whether the
#number is a multiple of 10 or not.

# Ask the user for a number

number = int(input("Enter a number: "))

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

#-----------------------------------------------------------------------------------------
#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza

# Prompt the user for pizza toppings
print("Enter pizza toppings one by one. Type 'quit' to finish.")

while True:
    topping = input("Enter a topping: ")

    if topping.lower() == 'quit':
        print("Finished adding toppings!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")

#-----------------------------------------------------------------------------------------
#7-5. Movie Tickets: A movie theater charges different ticket prices depending on
#a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
#$15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.

print("Welcome to the movie theater!")
print("Type 'quit' to exit at any time.\n")

while True:
    age_input = input("Please enter your age: ")

    if age_input.lower() == 'quit':
        print("Thank you for visiting. Enjoy the movie!")
        break

    if age_input.isdigit():
        age = int(age_input)
        if age < 3:
            print("The ticket is free.")
        elif 3 <= age <= 12:
            print("The ticket costs $10.")
        else:
            print("The ticket costs $15.")
    else:
        print("Please enter a valid age or 'quit' to exit.")

#-----------------------------------------------------------------------------------------
#7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
#that do each of the following at least once:
#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value.

#conditional test
age_input = input("Enter your age (or 'quit' to exit): ")
while age_input.lower() != 'quit':
    if age_input.isdigit():
        age = int(age_input)
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket costs $10.")
        else:
            print("The ticket costs $15.")
    else:
        print("Please enter a valid age.")

    age_input = input("Enter your age (or 'quit' to exit): ")
print("Thanks for using the ticket system!")

#active variable
active = True

while active:
    age_input = input("Enter your age (or 'quit' to exit): ")
    if age_input.lower() == 'quit':
        active = False
    elif age_input.isdigit():
        age = int(age_input)
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket costs $10.")
        else:
            print("The ticket costs $15.")
    else:
        print("Please enter a valid number.")
print("Session ended.")

#break statement
while True:
    age_input = input("Enter your age (or 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break
    elif age_input.isdigit():
        age = int(age_input)
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket costs $10.")
        else:
            print("The ticket costs $15.")
    else:
        print("Invalid input. Please enter a number.")
print("Goodbye!")

#-----------------------------------------------------------------------------------------
#7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
#ctrl-C or close the window displaying the output.)

# Infinite loop
while True:
    print("This loop will run forever. Press Ctrl+C to stop.")


#-----------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------
#7-10. Dream Vacation: Write a program that polls users about their dream
#vacation. Write a prompt similar to If you could visit one place in the world,
#where would you go? Include a block of code that prints the results of the poll.

# Dictionary to store responses
dream_vacations = {}

# Variable to control the loop
polling_active = True

# Start polling
while polling_active:
    # Ask for user name and dream vacation
    name = input("What is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    # Store the response
    dream_vacations[name] = destination

    # Ask if another person wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat.lower() != 'yes':
        polling_active = False

# Print poll results
print("\n--- Poll Results ---")
for name, destination in dream_vacations.items():
    print(f"{name.title()} would like to visit {destination.title()}.")