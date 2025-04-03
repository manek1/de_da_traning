#3-6. More Guests: You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
#statement to the end of your program informing people that you found a
#bigger dinner table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
guest_list = ["Amar", "Megha", "Madhuri", "Nilam"]

for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")

guest_unable = "Megha"
print(f"\nUnfortunately, {guest_unable} can't make it to the dinner.")

#replace guest
guest_list.remove(guest_unable)
guest_list.append("Sonali")

# Updated list
print("\n Sending new invitations:")
for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")



    # adding new guest beginning of list
print("\n Good news! I found a bigger dinner table, and there's room for more guests.")

guest_list.insert(0, "Ram")

# Using insert() to add a guest to the middle of the list
middle_guest = len(guest_list) // 2
guest_list.insert(middle_guest, "Manawa")

# Using append() to add a guest to the end of the list
guest_list.append("Shyam")

# Printing the new set of invitations
print("\nSending out new invitations:")
for guest in guest_list:
    print(f"Hi {guest}, I am inviting you to as a guest for dinner party!")