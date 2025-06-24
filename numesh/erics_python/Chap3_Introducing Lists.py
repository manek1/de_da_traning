# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

names = ['govind', 'numesh', 'madhuri']
print(names[0])
print(names[1])
print(names[2])

# from chatgpt
for name in names:
    print(name)

#--------------------------------------------------------------------------------------
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

names = ['govind', 'numesh', 'madhuri']

for name in names:
    print(f"my name is {name}")

#--------------------------------------------------------------------------------------
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

vehicle = ['Ford', 'Tata', 'Skoda']
for transportation in vehicle:
    print(f"I would like to own a {transportation} car")

#--------------------------------------------------------------------------------------
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner

dinner = ['madhuri', 'numesh', 'govind', 'sanket']
for people in dinner:
    print(f"hello {people}, I am inviting you to as a guest for dinner party.")

#--------------------------------------------------------------------------------------
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

guest_list = ['madhuri', 'numesh', 'govind', 'sanket']

for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

guest_unable = "sanket"
print(f"\nUnfortunately, {guest_unable} can't make it to the dinner.")

# replace guest
guest_list.remove(guest_unable)
guest_list.append("simran")

# Updated list
print("\n Sending new invitations:")
for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

#--------------------------------------------------------------------------------------
# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
guest_list = ['madhuri', 'numesh', 'govind', 'sanket']

for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

guest_unable = "sanket"
print(f"\nUnfortunately, {guest_unable} can't make it to the dinner.")

# replace guest
guest_list.remove(guest_unable)
guest_list.append("simran")

# Updated list
print("\n Sending new invitations:")
for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

    # adding new guest beginning of list
print("\n Good news! I found a bigger dinner table, and there's room for more guests.")

guest_list.insert(0, "Aishwarya")
# Using insert() to add a guest to the middle of the list
middle_guest = len(guest_list) // 2
guest_list.insert(middle_guest, "Pratibha")

# Using append() to add a guest to the end of the list
guest_list.append("Ujwal")

# Printing the new set of invitations
print("\nSending out new invitations:")
for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

#--------------------------------------------------------------------------------------
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

guest_list = ['madhuri', 'numesh', 'govind', 'sanket']

for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

print("\n unfortunetly i am inviting two people now due to new dinner table won’t arrive on time\n")

while len(guest_list) > 2:
    remove_guest = guest_list.pop()

    print(f"sorry {remove_guest} I can’t invite you to dinner.")

    del guest_list[:]

    # Printing the list to confirm it's empty
    print("\nFinal guest list:", guest_list)

#--------------------------------------------------------------------------------------
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

places = ['New York', 'Sydney', 'Paris', 'Tokyo', 'Cairo']
print(f"original list is {places}")

# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print("\n List in alphabetical order", sorted(places))

# Show that your list is still in its original order by printing it.
print("\n original list after sorted", places)

# Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
print("\n List in reverse order ", sorted(places, reverse=1))

# Show that the list is still in its original order
print("\nList after using sorted(reverse=True) (should be unchanged):")
print(places)

#  Use reverse() to change the order of the list
places.reverse()
print("\nList after using reverse() (order has changed):", places)

# Use reverse() to change the order of the list again (back to original order)
places.reverse()
print("\nList after using reverse() again (back to original order):", places)

# Use sort() to change the list so it's stored in alphabetical order
places.reverse()
print("\nList after using sort() (alphabetical order):", places)

#--------------------------------------------------------------------------------------
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

places = ['New York', 'sydney', 'Paris', 'Tokyo', 'Cairo']

# print a message indicating the number of people you are inviting to dinner
print(f"I am inviting {len(places)} people to dinner.")

#--------------------------------------------------------------------------------------
# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

# 1. Create a list of places
places = ['Rome', 'Sydney', 'London', 'Tokyo', 'Beijing']

# 2. Use len() to print the number of cities in the list
print(f"Number of places in the list: {len(places)}")

# 3. Use append() to add a new city to the list
places.append('Singapore')
print("\nAfter appending Singapore:")
print(places)

# 4. Use insert() to add a city at a specific position
places.insert(2, 'Delhi')
print("\nAfter inserting Delhi at index 2:")
print(places)

# 5. Use remove() to remove a specific city from the list
places.remove('Tokyo')
print("\nAfter removing Tokyo:")
print(places)

# 6. Use pop() to remove the last city from the list
last_city = places.pop()
print("\nAfter popping the last city:", last_city)
print(places)

# 7. Use sort() to sort the list alphabetically
places.sort()
print("\nAfter sorting alphabetically:")
print(places)

# 8. Use reverse() to reverse the order of the list
places.reverse()
print("\nAfter reversing the list:")
print(places)

# 9. Use sorted() to print the list in alphabetical order without changing the original list
print("\nSorted (without modifying original list):")
print(sorted(places))

# 10. Use reverse() again to change the order back to the original
places.reverse()
print("\nAfter reversing the list back to the original order:")
print(places)

# 11. Use count() to count how many times a certain city appears in the list
print("\nCount of 'London' in the list:", places.count('London'))

# 12. Use extend() to combine the cities list with another list of cities
more_cities = ['Mumbai', 'Kolkata']
places.extend(more_cities)
print("\nAfter extending the list with more cities:")
print(places)

#--------------------------------------------------------------------------------------
# 3-11. Intentional Error: If you haven’t received an index error in one of your
# programs yet, try to make one happen. Change an index in one of your programs
# to produce an index error. Make sure you correct the error before closing
# the program

# List of cities
places = ['Rome', 'Sydney', 'London', 'Tokyo', 'Beijing']
# Intentionally cause an IndexError by accessing an invalid index
try:
    print("\nAccessing an invalid index (7):")
    print(places[7])  # This will cause an IndexError because the list only has 5 elements
except IndexError as e:
    print(f"An error occurred: {e}")

    # Correcting the error by accessing a valid index
    print("\nNow accessing a valid index (2):")
    print(places[2])  # This will work, since index 2 is valid (London)
