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

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.

for num in range(1,21):
   print(num)

#4-4. One hundred: Make a list of the numbers from one to one hundred, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)

num_list=[]
for num in range(1,21):
    num_list.append(num)
print(num_list)

#4-5. Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.

print(min(num_list))
print(max(num_list))
print(sum(num_list))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_list=[]
for i in range(1,20,2):
    odd_list.append(i)
print(odd_list)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

threes=[]
for i in range(1,11):
    multiples_3=i*3
    threes.append(multiples_3)
print(threes)

#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

cubes=[]
for i in range(1,11):
    cube=i**3
    cubes.append(cube)
print(cubes)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.
cubes=[i**3 for i in range(1,11)]
print(cubes)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:•	 Print the message, The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
Pizza=['Dominos','Papa_Johns','Pizza_hut','MacD','Albayk']
print(Pizza)
print('The first three items in the list are :\n '+str(Pizza[:3]))

#Print the message, Three items from the middle of the list are:. Use a slice
#to print three items from the middle of the list
print('Three items from the middle of the list are:\n '+str(Pizza[1:4]))

#•	 Print the message, The last three items in the list are:. Use a slice to print
#the last three items in the list.
print('The last three items in the list are: \n'+str(Pizza[-3:]))

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:
my_pizzas = Pizza
print('My Pizzas : '+str(my_pizzas))
friend_pizzas=my_pizzas[:]
print('Friends pizzas: '+str(friend_pizzas))

#•	 Add a new pizza to the original list.
my_pizzas.append('Mushroom')
print('My Pizzas : '+str(my_pizzas))

#•	 Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Pepperoni')
print('Friends pizzas: '+str(friend_pizzas))

#Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message,
#My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print('My fav pizzas are : ')
for i in my_pizzas:
    print(i)
print('My friends fav pizzas are : ')
for i in friend_pizzas:
    print(i)


#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of fivesimple foods, and store them in a tuple.
buffet=('rice','roti','sabji','dal')

#Use a for loop to print each food the restaurant offers.
print ('The buffet options are: ')
for i in buffet:
    print(str(i.title()))

#The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for
#loop to print each of the items on the revised menu.
revised_menu=('papad','biriyani')
print('The revised menu is as follows: \n')
for food in revised_menu:
    print(str(food.title()))