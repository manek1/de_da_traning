#6-6. Polling: Use the code in favorite_languages.py (page 104).
#• Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have
#already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take
#the poll.

# Dictionary: names of people and their favorite programming languages
favorite_languages = {
    'Madhuri': 'python',
    'Amar': 'java',
    'Amit': 'c++',
    'Urmila': 'javascript'
}

# List of people who should take the poll (some are already in the dictionary)
people_to_poll = ['alice', 'bob', 'ethan', 'fiona', 'diana']

# Loop through the list of people to check if they've already taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, we invite you to take the favorite languages poll.")