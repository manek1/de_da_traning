"""4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza."""
Pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]
for pizza in Pizzas :
    print(pizza)

""""•	 Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza."""
for pizza in Pizzas :
    print("I like " + pizza + " pizza.")

"""•	 Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!"""
for pizza in Pizzas :
    print("I Like " + pizza + " pizza.")
print("I really love pizza!")

"""4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal."""
animals = ["Dog", "Cat", "Rabbit"]


"""•	 Modify your program to print a statement about each animal, such as
A dog would make a great pet."""
for animal in animals :
    print("A " + animal.lower() + "would make a great pet.")


"""•	 Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!"""
print("Any of these animals would make a great pet!")

"""4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
 inclusive."""
for number in range(1, 21) :
    print(number)

"""4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window."""
num_list=[]
for num in range(1,10000000):
    num_list.append(num)
print(num_list)

"""4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""
number = list(range(1,10))
print(min(number))
print(max(number))
print(sum(number))

"""4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number."""
odd_number =[]
for odd_no in range(1, 21, 2) :
    odd_number.append(odd_no)
print(odd_number)

"""4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list."""
threes = []
for three in range(1, 11) :
    multi = three*3
    threes.append(multi)
print(threes)

"""4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube."""
cubess = []
for cubes in range(1, 11) :
    cube = cubes**3
    cubess.append(cube)
print(cubess)

"""4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes."""
cubess = [cubes**3 for cubes in range(1, 11)]
print(cubess)

"""4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:"""

"""Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list."""
IPL = ["GT", "RCB", "PBKS", "MI", "DC"]
print(IPL)
print("The first three qualify teams in this IPL Tournament is : " + str(IPL[:3]))

"""•	 Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list."""

print("The three middle qualify teams in this IPL Tournament is : " + str(IPL[1:4]))

"""Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list."""
IPL = ["GT", "RCB", "PBKS", "MI", "DC", "LSG", "KKR", "SRH", "RR", "CSK"]
print("The last three eliminate teams are : " +str(IPL[-3:]))

"""4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:"""
my_team = IPL
print("My Teams : " + str(my_team))
friend_team = my_team [:]
print("Friends Teams : " + str(friend_team))

"""Add a new pizza to the original list."""
my_team.append("KT")
print("My Teams : " + str(my_team))

"""•	 Add a different pizza to the list friend_pizzas"""
friend_team.append("GL")
print("Friends_Teams : " + str(friend_team))

""""•	 Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list."""
print("My fvt teams are : ")
for i in my_team :
  print(i)
print("MY friends fvt teams are : ")
for i in friend_team :
  print(i)

"""4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
"""
buffet_foods = ("rice", "noodles", "salad", "soup", "fruit")

"""•	 Use a for loop to print each food the restaurant offers"""
print("The buffet offers the following foods : ")
for food in buffet_foods:
    print(food)

"""The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu."""
revised_menu=('papad','biriyani')
print('The revised menu is as follows: \n')
for food in revised_menu:
    print(str(food.title()))
