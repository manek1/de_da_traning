class User:
    def __init__(self,first_name,last_name,dob,gender,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.dob=dob
        self.gender=gender
        self.login_attempts=login_attempts

    def describe_user(self):
        print("The user's name is : "+self.first_name+''+self.last_name +"\n The birthdate is :"+self.dob+'\n The gender is : '+self.gender)
    def greet_user(self):
        print('Hi '+self.first_name+" "+self.last_name+'! It is wonderful to have you on board!')
    def increment_login_attempts(self):
        incremented_value_of_login_attempt=self.login_attempts+1
        print("The incremented value of login attempts is :"+str(incremented_value_of_login_attempt))
    def reset_login_attempts(self):
        login_attempts=0
        print("The login attempt have been reset to 0")