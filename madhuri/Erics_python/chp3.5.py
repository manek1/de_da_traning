#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#• Start with your program from Exercise 3-4. Add a print statement at the
#end of your program stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still
#in your list.



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

