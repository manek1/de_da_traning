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

user_number=input("Please enter a number of your choice and I will tell if its a multiple of 10. Your number =  ")
user_number=int(user_number)
if user_number%10 ==0:
    print("The number you have entered "+str(user_number)+" is a multiple of 10.")
else:
    print("The number you have entered " + str(user_number) + " is NOT a multiple of 10.")