#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
#names to use as keys in the dictionary, and store one to three favorite places
#for each person. To make this exercise a bit more interesting, ask some friends
#to name a few of their favorite places. Loop through the dictionary, and print
#each person’s name and their favorite places.

# Create a dictionary with people's names as keys and lists of favorite places as values
favorite_places = {
    'alice': ['paris', 'tokyo', 'new york'],
    'bob': ['london'],
    'charlie': ['rome', 'barcelona']
}

# Loop through the dictionary to print each person's favorite places
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite place(s):")

    # Loop through the list of places for each person
    for place in places:
        print(f"  - {place.title()}")  # Format each place nicely

    print()  # Add a blank line between entries