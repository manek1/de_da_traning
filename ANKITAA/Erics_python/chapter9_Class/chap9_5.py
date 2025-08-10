#9-5. Login Attempts: Add an attribute called login_attempts to your User
#class from Exercise 9-3 (page 166). Write a method called increment_
#login_attempts() that increments the value of login_attempts by 1. Write
#another method called reset_login_attempts() that resets the value of login_
#attempts to 0.
#Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented
#properly, and then call reset_login_attempts(). Print login_attempts again to
#make sure it was reset to 0.

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # New attribute with default value

    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        print(f"Login Attempts: {self.login_attempts}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating a user instance
user = User("Diana", "Cruz", 30, "diana.cruz@example.com", "Miami")

# Simulate login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login attempts
print(f"Login attempts after increments: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()

# Print login attempts after reset
print(f"Login attempts after reset: {user.login_attempts}")