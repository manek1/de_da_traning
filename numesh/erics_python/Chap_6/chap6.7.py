#6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
#Make two new dictionaries representing different people, and store all three
#dictionaries in a list called people. Loop through your list of people. As you
#loop through the list, print everything you know about each person.

# Define three dictionaries representing different people
person1 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

person2 = {
    'first_name': 'Bob',
    'last_name': 'Smith',
    'age': 35,
    'city': 'London'
}

person3 = {
    'first_name': 'Clara',
    'last_name': 'Wang',
    'age': 22,
    'city': 'Beijing'
}

# Store all three people in a list
people = [person1, person2, person3]

# Loop through the list and print information about each person
for person in people:
    # Print each key-value pair in the current person's dictionary
    print("Person Info:")
    for key, value in person.items():
        # Capitalize the key for display
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()  # Add a blank line between people for readability
