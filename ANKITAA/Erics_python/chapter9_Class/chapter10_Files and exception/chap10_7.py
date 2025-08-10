#10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
#so the user can continue entering numbers even if they make a mistake and
#enter text instead of a number.

print("Welcome to the Addition Calculator!")
print("Type 'quit' at any time to exit.\n")

while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'quit':
        break

    num2 = input("Enter the second number: ")
    if num2.lower() == 'quit':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print(" Invalid input! Please enter **numbers only**.\n")
    else:
        print(f"The sum of {num1} and {num2} is {result}.\n")