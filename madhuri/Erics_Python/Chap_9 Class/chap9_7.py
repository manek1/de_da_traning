#9-7. Admin: An administrator is a special kind of user. Write a class called
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
#or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
#of strings like "can add post", "can delete post", "can ban user", and so on.
#Write a method called show_privileges() that lists the administrator’s set of
#privileges. Create an instance of Admin, and call your method.

# Parent Class: User
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0  # Included from Exercise 9-5

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

# Subclass: Admin
class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords"
        ]

    def show_privileges(self):
        print(f"Admin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()  # Extra line for spacing

# Creating an Admin instance
admin_user = Admin("Laura", "Stevens", 40, "laura.admin@example.com", "San Francisco")

# Calling the show_privileges() method
admin_user.show_privileges()
