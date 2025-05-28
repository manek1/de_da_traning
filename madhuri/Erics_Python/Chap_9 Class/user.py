#9-12. Multiple Modules: Store the User class in one module, and store the
#Privileges and Admin classes in a separate module. In a separate file, create
#an Admin instance and call show_privileges() to show that everything is still
#working correctly.

# user.py

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

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
