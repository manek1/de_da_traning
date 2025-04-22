'''9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly'''

from Res import Restaurant
my_res=Restaurant('Mubasheer','Arabic Cuisine')
my_res.describe_restaurant()

'''9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly.'''

from admin_related_classes import User
from admin_related_classes import Privileges
from admin_related_classes import Admin
user1=Admin('Leela','Maaney','220396','F','8')
user1.priv.show_privileges()

'''9-12. Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create 
an Admin instance and call show_privileges() to show that everything is still 
working correctly.'''
from admin_and_priv import Admin
from admin_and_priv import Privileges
from user_class import User
print("#################This is the ouput for the 9-12 ")
a3=Admin('Manoj','Nair','230598','M','10')
a3.priv.show_privileges()