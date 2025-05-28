#chap 9.12
# admin_privileges.py

from user import User  # Importing User class from user.py

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user", "can reset passwords"]
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
        print()  # Extra line for spacing

class Admin(User):  # Admin inherits from User class
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()  # Admin has an instance of Privileges
