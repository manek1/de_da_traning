"""Chap-3 Introducing Lists (List,Changing,Adding,Removing Elements,Organizing a List,
Avoiding Index Error when working with Lists"""

"""3-1. Names: Store the names of a few of your friends in a list called names. Print
each person’s name by accessing each element in the list, one at a time."""

friends = ['Sujay','Nadeem','Kiran','Prashant']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

"""3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the
person’s name."""

friends = ['Sujay','Nadeem','Kiran','Prashant']
print("Hello, " + friends[0].title() + ", Vijay Trophy matches are going to start from next month.")
print("Hello, " + friends[1].title() + ", Vijay Trophy matches are going to start from next month.")
print("Hello, " + friends[2].title() + ", Vijay Trophy matches are going to start from next month.")
print("Hello, " + friends[-1].title() + ", Vijay Trophy matches are going to start from next month.")

print("Hello, " + friends[0].title() + "," + friends[1].title() + "," + friends[2].title() + " And "
      + friends[-1].title() + " Vijay Trophy matches are going to start from next month.")

"""3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""
vehicles = ["Lamborghini Urus", "BMW M5", "Mercedes-Benz S-Class  S580", "Mercedes-Benz GLS 400 D",
            "Land Rover Range Rover HSE LWB", "Skoda Octavia", "Toyota Fortuner"]
print("Rohit Sharma's car collection includes luxury vehicles like the" " " + vehicles[0] + "," +vehicles[1] + ","
      + vehicles[2] + " " "And" +vehicles[4] + '.')

"""3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner."""

guests = ["Rohit Sharma", "Virat Kohli", "AB DE Villiers", "Kane Williamson"]
print("Dear " + guests[0] + "," + guests[1] + "," + guests[2] + " And " + guests[3] +
      ", I would be honored to have you for dinner.")
print("Dear " + guests[0] + " , I would be honored to have you for dinner.")
print("Dear " + guests[1] + " , I would be honored to have you for dinner.")
print("Dear " + guests[2] + " , I would be honored to have you for dinner.")
print("Dear " + guests[3] + " , I would be honored to have you for dinner.")


"""3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list."""

print("Dear " + guests[0] + "," + guests[1] + "," + guests[2] + " And " + guests[3] + ".")
print("Unfortunately" + guests[3] + "can't make it to dinner.")
guests = ["Rohit Sharma", "Virat Kohli", "AB DE Villiers", "Pat Cummins"]
print("Dear " + guests[0] + "," + guests[1] + "," + guests[2] + " And " + guests[3] +
      ", I would be honored to have you for dinner.")

"""3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list"""

guests = ["Rohit Sharma", "Virat Kohli", "AB DE Villiers", "Pat Cummins"]
print("Good news! I found a bigger dinner table, so I’m inviting more guests.")
guests.insert(0 ,"Devid Miller")
guests.insert(3 , "Jeo Root")
guests.append("Devid Warner")
print("Dear " + guests[0] + "," +guests[1] + "," + guests[2] + "," + guests[3] + "," + guests[4] + ","
      + guests[5] + "," + guests[6] + " , you are cordially invited to dinner.")

"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""

print("Unfortunately, the new dinner table won’t arrive on time. I can invite only two people for dinner.")
last_guests = guests.pop()
print("Sorry " + last_guests + " , I can't invite you to dinner.")
print(guests)

last_guests = guests.pop()
print("Sorry " + last_guests + " , I can't invite you to dinner.")
print(guests)

last_guests = guests.pop()
print("Sorry " + last_guests + " , I can't invite you to dinner.")
print(guests)

last_guests = guests.pop()
print("Sorry " + last_guests + " , I can't invite you to dinner.")
print(guests)

last_guests = guests.pop()
print("Sorry " + last_guests + " , I can't invite you to dinner.")
print(guests)

"""Print a message to each of the two people still on your list, letting them know they’re still invited."""
print("Dear " + guests[0] + " And " + guests[1] + " ,you're still invited to dinner.")

"""Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
#of your program."""

del(guests[0])
del(guests[0])
print(guests)

"""3-8. Seeing the World: Think of at least five places in the world you’d like to
visit."""

"""•	 Store the locations in a list. Make sure the list is not in alphabetical order"""
places_to_visit = ["Japan", "Norway", "New Zealand", "Canada", "Switzerland"]

"""•	 Print your list in its original order. Don’t worry about printing the list neatly,
 just print it as a raw Python list."""
print(places_to_visit)

"""Use sorted() to print your list in alphabetical order without modifying the actual list."""
print(sorted(places_to_visit))

"""Show that your list is still in its original order by printing it."""
print(places_to_visit)

"""Use sorted() to print your list in reverse alphabetical order without changing the order of the original list."""
new_place_list= [item.lower() for item in places_to_visit]
print(new_place_list)
print(sorted(new_place_list))
sorted_list=sorted(new_place_list)
sorted_list.reverse()
print(sorted_list)

"""•	 Show that your list is still in its original order by printing it again."""
print(places_to_visit)

"""•	 Show that your list is still in its original order by printing it again."""
places_to_visit.reverse()
print(places_to_visit)

"""•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order."""
places_to_visit.reverse()
print(places_to_visit)

"""Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed."""
print(new_place_list)
new_place_list.sort()
print(new_place_list)

"""Use sort() to change your list so it’s stored in reverse alphabetical order.Print the list to show 
that its order has changed."""
new_place_list.sort(reverse=True)
print(new_place_list)

"""3-9 use len() to print a message indicating the number of people you are inviting to dinner."""
count_places=len(new_place_list)










