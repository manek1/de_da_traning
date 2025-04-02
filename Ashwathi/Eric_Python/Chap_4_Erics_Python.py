#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
Pizza=['Dominos','Papa_Johns','Pizza_hut']
for i in Pizza:
    print(i)

#Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
for i in Pizza:
    print('I love '+i+'!')

#Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines
#about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
for i in Pizza:
    print('I love '+i+'!')
print('Anything in Cheese burst is favourite!\nHowever it should be filling too!')

#4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

animals=['cat','dog','parrot']
for i in animals:
    print('A '+i+' would make a great pet!')
print('These are most commonly pet animals')