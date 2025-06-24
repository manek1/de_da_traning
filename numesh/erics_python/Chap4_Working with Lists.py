#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza
#instead of printing just the name of the pizza. For each pizza you should
#have one line of output containing a simple statement like I like pepperoni
#pizza.
#• Add a line at the end of your program, outside the for loop, that states
#how much you like pizza. The output should consist of three or more lines
#about the kinds of pizza you like and then an additional sentence, such as
#I really love pizza!


pizzas = ["simple_veg", "corn", "Mixtopping"]

#Use a for loop to print the name of each pizza
for pizza in pizzas:
    print(pizza)

# Modify the loop to print a sentence using the name of each pizza
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Add a statement outside the loop about how much you like pizza
print("I really love pizza!")

#--------------------------------------------------------------------------------------
#4-2. Animals: Think of at least three different animals that have a common characteristic.
#Store the names of these animals in a list, and then use a for loop to
#print out the name of each animal.
#• Modify your program to print a statement about each animal, such as
#A dog would make a great pet.
#• Add a line at the end of your program stating what these animals have in
#common. You could print a sentence such as Any of these animals would
#make a great pet!

animals=["dog","cat","cow","rabbit"]
for animal in animals:
    print(f"{animal}")

     #• Modify your program to print a statement about each animal
for animal in animals:
   print(f"a {animal} would make a great pet")

 # add sentence
print("\n Any of these animals would make a great pet!")

#--------------------------------------------------------------------------------------
#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
#inclusive.

for number in range(1,21):
    print(number)

#--------------------------------------------------------------------------------------
#4-4. One Million: Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers. (If the output is taking too long, stop it by
#pressing ctrl-C or by closing the output window.

numbers=list(range(1,1000001))

for number in numbers:
    print(number)

#--------------------------------------------------------------------------------------
#4-5. Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list actually starts at one and
#ends at one million. Also, use the sum() function to see how quickly Python can
#add a million numbers.

numbers=list(range(1,1000001))

print("The minimum number is:",min(numbers))
print("The maximum number is:",max(numbers))
print("The sum of number is:",sum(numbers))

#--------------------------------------------------------------------------------------
#4-6. Odd Numbers: Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_num=range(1,21,2)
for number in odd_num:
    print(number)

#--------------------------------------------------------------------------------------
#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
#print the numbers in your list.

numbers=range(3,31,3)
for num in numbers:
    print(num)

#--------------------------------------------------------------------------------------
#4-8. Cubes: A number raised to the third power is called a cube. For example,
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube

cubes = [number**3 for number in range(1, 11)]

# Use a for loop to print the cube of each number
for cube in cubes:
    print(cube)

#--------------------------------------------------------------------------------------
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the
#first 10 cubes.

cubes = [number**3 for number in range(1, 11)]

# Use a list comprehension to generate a list of the first 10 cubes
print(cubes)

#--------------------------------------------------------------------------------------
#4-10. Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:
#• Print the message, The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
#• Print the message, Three items from the middle of the list are:. Use a slice
#to print three items from the middle of the list.
#• Print the message, The last three items in the list are:. Use a slice to print
#the last three items in the list.

# Define a list of favorite foods
foods = ['pizza', 'burger', 'pasta', 'sushi', 'tacos', 'noodles']

# Print the first three items in the list
print("The first three items in the list are:", foods[:3])

# Print three items from the middle of the list
middle_index = len(foods) // 2  # Find the middle index
print("Three items from the middle of the list are:", foods[middle_index-1:middle_index+2])

# Print the last three items in the list
print("The last three items in the list are:", foods[-3:])

#--------------------------------------------------------------------------------------
#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
#(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
#Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message, My favorite
#pizzas are:, and then use a for loop to print the first list. Print the message,
#My friend’s favorite pizzas are:, and then use a for loop to print the second
#list. Make sure each new pizza is stored in the appropriate list.

pizzas = ["simple_veg", "corn", "Mixtopping", "onion"]

# Copy the list
friend_pizzas = pizzas[:]

# Add different pizzas
pizzas.append("paneer")
friend_pizzas.append("chicken")

# Print my favorite pizzas
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Print my friend's favorite pizzas
print("My friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#--------------------------------------------------------------------------------------
#4-12. More Loops: All versions of foods.py in this section have avoided using
#for loops when printing to save space. Choose a version of foods.py, and
#write two for loops to print each list of foods.

my_foods = ['pizza', 'burger', 'cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

#--------------------------------------------------------------------------------------
#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#simple foods, and store them in a tuple.
#• Use a for loop to print each food the restaurant offers.
#• Try to modify one of the items, and make sure that Python rejects the
#change.
#• The restaurant changes its menu, replacing two of the items with different
#foods. Add a block of code that rewrites the tuple, and then use a for
#loop to print each of the items on the revised menu.

# Initial buffet menu
buffet = ("pasta", "salad", "soup", "bread", "rice")

print("The restaurant offers the following foods:")
for food in buffet:
    print(food)

# Try to modify an item (will cause an error if uncommented)
# buffet[0] = "pizza"  # Tuples are immutable

# Changing the menu (creating a new tuple)
buffet = ("pasta", "salad", "fries", "cake", "rice")

print("\nThe new restaurant menu is:")
for food in buffet:
    print(food)


