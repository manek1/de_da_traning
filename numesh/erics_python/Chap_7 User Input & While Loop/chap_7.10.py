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
