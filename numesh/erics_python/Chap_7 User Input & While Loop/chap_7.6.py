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

