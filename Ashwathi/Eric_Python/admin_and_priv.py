from user_class import User
class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for i in self.privileges:
            print('This is the method from the Privileges class. The admin can '+i)

class Admin(User):
    def __init__(self,first_name,last_name,dob,gender,login_attempts):
        super().__init__(first_name,last_name,dob,gender,login_attempts)
        #Privileges instance as an attribute in the Admin class
        self.priv=Privileges()