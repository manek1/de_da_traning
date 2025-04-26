#4-10. Slices: Using one of the programs you wrote in this chapter, add several
#lines to the end of the program that do the following:
#• Print the message, The first three items in the list are:. Then use a slice to
#print the first three items from that program’s list.
#• Print the message, Three items from the middle of the list are:. Use a slice
#to print three items from the middle of the list.
#• Print the message, The last three items in the list are:. Use a slice to print
#the last three items in the list.

# List of favorite fruits
favorite_fruits = ['mango', 'banana', 'strawberry', 'apple', 'grape', 'pineapple', 'orange']

# Print the first three items
print("The first three items in the list are:")
print(favorite_fruits[:3])  # Indexes 0, 1, 2

# Print three items from the middle
print("Three items from the middle of the list are:")
middle_index = len(favorite_fruits) // 2  # Middle of the list
print(favorite_fruits[middle_index - 1:middle_index + 2])  # E.g. indexes 2, 3, 4

# Print the last three items
print("The last three items in the list are:")
print(favorite_fruits[-3:])  # Last three elements