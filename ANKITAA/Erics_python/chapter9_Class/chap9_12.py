#chap_9.12

# main.py

from admin_privileges import Admin  # Import Admin from admin_privileges.py

# Creating an Admin instance
admin_user = Admin("Alice", "Smith", 40, "alice.smith@example.com", "Los Angeles")

# Calling the method to show privileges
admin_user.privileges.show_privileges()