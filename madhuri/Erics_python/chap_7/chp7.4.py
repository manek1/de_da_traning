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