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
