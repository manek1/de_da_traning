#6-8. Pets: Make several dictionaries, where the name of each dictionary is the
#name of a pet. In each dictionary, include the kind of animal and the owner’s
#name. Store these dictionaries in a list called pets. Next, loop through your list
#and as you do print everything you know about each pet.

# Create dictionaries for different pets
tommy = {
    'animal': 'dog',
    'owner': 'Alice'
}

mau = {
    'animal': 'cat',
    'owner': 'Bob'
}

nemo = {
    'animal': 'fish',
    'owner': 'Charlie'
}

bella = {
    'animal': 'rabbit',
    'owner': 'Diana'
}

# Store all pet dictionaries in a list
pets = [tommy, mau, nemo, bella]

# Loop through the list and print information about each pet
for pet in pets:
    print("Pet Info:")
    for key, value in pet.items():
        # Print each key-value pair with a neat format
        print(f"  {key.title()}: {value}")
    print()  # Add a blank line between pets
