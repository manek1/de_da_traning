#3-1.  Names:  Store the names of a few of your friends in a list called  names  Print each person’s name by accessing each element in the list, one at a time
friends=['Ash', 'chandni','monica','Prajakta','Shamli']
print(friends[0])
print(friends[-1])
print(friends[1])
print(friends[2])
print(friends[3])

#3-2.  Greetings:  Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them  The text of each mes-sage should be the same, but each message should be personalized with the person’s name

print('I love my girls: '+ friends[1].title()+','+friends[2].title()+','+friends[3]+' and '+friends[-1])

#3-3.  Your Own List:  Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples  Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle ”

vehicles=['Dio','Kia','Ford','G-wagon']
print('Ash had a black '+vehicles[0]+' in Baramati'+' and Pramod a black '+vehicles[1]+'.'+'Currently the red '+vehicles[2]+' is a saviour!'+'But he does hope to get a '+vehicles[3]+'!')

#3-4. G uest List:  If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner  Then use your list to print a message to each person, inviting them to dinner
guest_list=['Priyanka','Gandhiji','Hitler','Abdul Kalam']
print('Hi '+guest_list[0]+','+guest_list[1]+','+guest_list[2]+' and '+guest_list[3]+'. I would love for you to visit my home! ')

#3-5.  Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations  You’ll have to think of someone else to invite
print('Hi '+guest_list[0]+','+guest_list[1]+','+guest_list[2]+' and '+guest_list[3]+'.')
print('Unfortunately, '+guest_list[2] +' is unable to come.')
guest_list=['Gandhiji','Priyanka','Aish','Abdul Kalam']
print('Hi '+guest_list[0]+','+guest_list[1]+','+guest_list[2]+','+guest_list[2]+' and '+guest_list[3]+'. I would love for you to visit my home! ')

#3-6.  More Guests: You just found a bigger dinner table, so now more space is available  Think of three more guests to invite to dinner
print('Guys I found a bigger table! ')
guest_list.insert(0,'Sushmita')
guest_list.insert(3,'Lara')
guest_list.append('Manju')
print('Hi '+guest_list[0]+','+guest_list[1]+','+guest_list[2]+','+guest_list[3]+','+guest_list[4]+','+guest_list[5]+' and '+guest_list[6]+'. I would love for you to visit my home! ')

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print ('Hi guys! So sorry but I can accomodate only 2 people!')
last_guest_list=guest_list.pop()
print('Sorry '+ last_guest_list +' .Lets catchup next time ')
print(guest_list)
last_guest_list=guest_list.pop()
print('Sorry '+ last_guest_list +' .Lets catchup next time ')
print(guest_list)
last_guest_list=guest_list.pop()
print('Sorry '+ last_guest_list +' .Lets catchup next time ')
print(guest_list)
last_guest_list=guest_list.pop()
print('Sorry '+ last_guest_list +' .Lets catchup next time ')
print(guest_list)
last_guest_list=guest_list.pop()
print('Sorry '+ last_guest_list +' .Lets catchup next time ')
print(guest_list)

#Print a message to each of the two people still on your list, letting them know they’re still invited.
print(guest_list[0]+' and '+guest_list[1]+' ,you guys are still invited. Please come!')

#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end
#of your program.

del(guest_list[0])
del(guest_list[0])
print(guest_list)

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit. Store the locations in a list. Make sure the list is not in alphabetical order.
place_list=['Finland','Singapore','Bahamas','Canada']

#•	 Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(place_list)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(place_list))

#Show that your list is still in its original order by printing it.
print(place_list)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
new_place_list= [item.lower() for item in place_list]
print(new_place_list)
print(sorted(new_place_list))
sorted_list=sorted(new_place_list)
sorted_list.reverse()
print(sorted_list)

#•	 Show that your list is still in its original order by printing it again.
print(place_list)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
place_list.reverse()
print(place_list)

#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
place_list.reverse()
print(place_list)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print(new_place_list)
new_place_list.sort()
print(new_place_list)

#Use sort() to change your list so it’s stored in reverse alphabetical order.Print the list to show that its order has changed.
new_place_list.sort(reverse=True)
print(new_place_list)

#3-9 use len() to print a message indicating the number of people you are inviting to dinner.
count_places=len(new_place_list)
print('Currently, I wish to visit a total of '+ str(count_places) +' places!')





