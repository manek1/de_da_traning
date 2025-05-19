'''7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”'''

#user_car_preference=input("What kind of rental car would you like? ")
#print("Let me see if I can find you a "+user_car_preference+'.')

'''7-2. Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message say
ing they’ll have to wait for a table. Otherwise, report that their table is ready'''
'''
user_diner_number=input("Hi! Welcome. Could you please insert how many people are in your diner group? ")
user_diner_number=int(user_diner_number)
if user_diner_number>8:
    print("You are a total of "+str(user_diner_number)+" people. Kindly wait until we have a table for you!")
else:
    print("Your table is ready!") '''

'''7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
number is a multiple of 10 or not.'''
'''
user_number=input("Please enter a number of your choice and I will tell if its a multiple of 10. Your number =  ")
user_number=int(user_number)
if user_number%10 ==0:
    print("The number you have entered "+str(user_number)+" is a multiple of 10.")
else:
    print("The number you have entered " + str(user_number) + " is NOT a multiple of 10.")
'''
'''7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.'''
'''
prompt = "Please enter your choice of topping: "
prompt+="\n Enter 'quit' when you are finished."
while True:
    topping=input(prompt)
    if topping=='quit':
        break
    else:
        print("I will add the topping :"+topping+" to your Pizza!")
'''
'''7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
a person’s age. If a person is under the age of 3, the ticket is free; if they are 
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
$15. Write a loop in which you ask users their age, and then tell them the cost 
of their movie ticket.'''

prompt="Enter your age and I shall tell the movie fare. "
prompt+="\nEnter 'quit' to exit."

while True:
    person_age=input(prompt)

    if (prompt=='quit'):
        break
    elif (int(person_age)<3):
        print("Your age is less than 3 so the ticket is free.")
    elif (3<=int(person_age)<=12):
        print("Your age is in the range 3-12, so the ticket price  is 10.")
    elif (12<int(person_age)):
        print("Your age is greater than 12,so the ticket price  is 15.")


