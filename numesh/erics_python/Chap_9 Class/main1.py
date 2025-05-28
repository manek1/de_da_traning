#chap_9.11

# main.py

from user_privileges import Admin

# Creating an Admin instance
admin_user = Admin("Sarah", "Johnson", 35, "sarah.johnson@example.com", "New York")

# Calling the method to show privileges
admin_user.privileges.show_privileges()
