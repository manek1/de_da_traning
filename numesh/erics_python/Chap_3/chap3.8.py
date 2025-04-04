#3-8. Seeing the World: Think of at least five places in the world you’d like to
#visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly,
#just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the
#actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse alphabetical order without changing
#the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
#• Use reverse() to change the order of your list again. Print the list to show
#it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed.

places=['New York','Sydney','Paris','Tokyo','Cairo']
print(f"original list is {places}")

#Use sorted() to print your list in alphabetical order without modifying the
#actual list.
print("\n List in alphabetical order",sorted(places))

#Show that your list is still in its original order by printing it.
print("\n original list after sorted",places)

# Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
print("\n List in reverse order ",sorted(places,reverse=1))

# Show that the list is still in its original order
print("\nList after using sorted(reverse=True) (should be unchanged):")
print(places)

#  Use reverse() to change the order of the list
places.reverse()
print("\nList after using reverse() (order has changed):",places)


 #Use reverse() to change the order of the list again (back to original order)
places.reverse()
print("\nList after using reverse() again (back to original order):",places)


# Use sort() to change the list so it's stored in alphabetical order
places.reverse()
print("\nList after using sort() (alphabetical order):",places)