#10-4. Guest Book: Write a while loop that prompts users for their name. When
#they enter their name, print a greeting to the screen and add a line recording
#their visit in a file called guest_book.txt. Make sure each entry appears on a
#new line in the file.

# Guest Book Program
filename = 'guest_book.txt'

print("Welcome to the guest book!")
print("Enter 'quit' at any time to stop.\n")

while True:
    name = input("Please enter your name: ")

    if name.lower() == 'quit':
        print("Thank you! Guest book updated.")
        break

    # Print greeting
    print(f"Hello, {name}! You've been added to the guest book.")

    # Append name to the guest_book.txt file
    with open(filename, 'a') as file:
        file.write(f"{name}\n")