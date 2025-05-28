#9-8. Privileges: Write a separate Privileges class. The class should have one
#attribute, privileges, that stores a list of strings as described in Exercise 9-7.
#Move the show_privileges() method to this class. Make a Privileges instance
#as an attribute in the Admin class. Create a new instance of Admin and use your
#method to show its privileges.

# Parent class: User
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

# New class: Privileges
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()  # Extra spacing

# Subclass: Admin
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()  # Composition: privileges is an instance of Privileges

# Creating an Admin instance
admin_user = Admin("Kevin", "Lee", 38, "kevin.lee@example.com", "Seattle")

# Display the admin's privileges
admin_user.privileges.show_privileges()
