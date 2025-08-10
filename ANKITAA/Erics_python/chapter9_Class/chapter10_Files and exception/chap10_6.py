#10-6. Addition: One common problem when prompting for numerical input
#occurs when people provide text instead of numbers. When you try to convert
#the input to an int, you’ll get a TypeError. Write a program that prompts for
#two numbers. Add them together and print the result. Catch the TypeError if
#either input value is not a number, and print a friendly error message. Test your
#program by entering two numbers and then by entering some text instead of a
#number.

print("Let's add two numbers!")
print("Type 'quit' to exit.\n")

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
        print("Oops! Please enter **valid numbers** only.\n")
    else:
        print(f"The sum of {num1} and {num2} is {result}.\n")