#10-13. Verify User: The final listing for remember_me.py assumes either that the
#user has already entered their username or that the program is running for the
#first time. We should modify it in case the current user is not the person who
#last used the program.
#Before printing a welcome back message in greet_user(), ask the user if
#this is the correct username. If it’s not, call get_new_username() to get the correct
#username.
import json

FILENAME = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    """Prompt user to enter a new username and save it."""
    username = input("What is your name? ")
    with open(FILENAME, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user and verify if the stored username is correct."""
    username = get_stored_username()
    if username:
        is_correct = input(f"Are you {username}? (yes/no): ").strip().lower()
        if is_correct == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# Run the program
greet_user()
