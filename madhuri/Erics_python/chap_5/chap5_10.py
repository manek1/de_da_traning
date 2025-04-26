#5-10. Checking Usernames: Do the following to create a program that simulates
#how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. Make sure one or
#two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already
#been used. If it has, print a message that the person will need to enter a
#new username. If a username has not been used, print a message saying
#that the username is available.
#• Make sure your comparison is case insensitive. If 'John' has been used,
#'JOHN' should not be accepted.

# List of current usernames
current_users = ['alice', 'bob', 'john', 'mary', 'susan']

# List of new usernames
new_users = ['alice', 'dave', 'John', 'emma', 'BOB']

# Loop through the new_users list to check each username
for new_user in new_users:
    # Convert to lowercase to ensure case-insensitive comparison
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")