#10-3. Guest: Write a program that prompts the user for their name. When they
#respond, write their name to a file called guest.txt.

# Ask the user for their name
name = input("Please enter your name: ")

# Write the name to guest.txt
with open("guest.txt", "w") as file:
    file.write(name)

print(f"Thank you, {name} Your name has been recorded in guest.txt.")

