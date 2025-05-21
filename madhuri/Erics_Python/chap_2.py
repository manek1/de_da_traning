#2.1. Simple Message: Store a message in a variable, and then print that message.--

name="my name is numesh"
print (name)

--------------------------------------------------------------------------------------
#2-2. Simple Messages: Store a message in a variable, and print that message.
     #Then change the value of your variable to a new message, and print the new message

country="india is my country"
print (country)

country="bharat is my country"
print (country)

--------------------------------------------------------------------------------------
#2-3. Personal Message: Store a person’s name in a variable, and print a message
#to that person. Your message should be simple, such as, “Hello Eric,
#would you like to learn some Python today?”

p_name="eric"
message=f"hello {p_name},would you like to learn some Python today?"

print(message)

--------------------------------------------------------------------------------------
#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
#name in lowercase, uppercase, and titlecase.

name="indrajeet"

print(name.lower())
print(name.upper())
print(name.title())

--------------------------------------------------------------------------------------
#2-5. Famous Quote: Find a quote from a famous person you admire. Print the
#quote and the name of its author. Your output should look something like the
#following, including the quotation marks:
#Albert Einstein once said, “A person who never made a
#mistake never tried anything new.”

author="Albert Einstein"
quote='"A person who never made a mistake never tried anything new."'

print(f'{author} once said,{quote}')

--------------------------------------------------------------------------------------
#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s
#name in a variable called famous_person. Then compose your message
#and store it in a new variable called message. Print your message.

famous_person="Albert Einstein"
message='"A person who never made a mistake never tried anything new."'

print(f'{famous_person} once said,{message}')

--------------------------------------------------------------------------------------
#2-7. Stripping Names: Store a person’s name, and include some whitespace
#characters at the beginning and end of the name. Make sure you use each
#character combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip().


p_name="\t\narun\t\n"
print (p_name)
print (p_name.lstrip())
print (p_name.rstrip())
print (p_name.strip())

--------------------------------------------------------------------------------------
#2-8. Number Eight: Write addition, subtraction, multiplication, and division
#operations that each result in the number 8. Be sure to enclose your operations
#in print statements to see the results. You should create four lines that look
#like this:
#print(5 + 3)
#Your output should simply be four lines with the number 8 appearing once
#on each line.

print(4+4)
print(11-3)
print(4*2)
print(24/3)

--------------------------------------------------------------------------------------
#2-9. Favorite Number: Store your favorite number in a variable. Then, using
#that variable, create a message that reveals your favorite number. Print that
#message.

favourite_no=7
print(f"Favourite_no is {favourite_no}")

--------------------------------------------------------------------------------------
#2-10. Adding Comments: Choose two of the programs you’ve written, and
#add at least one comment to each. If you don’t have anything specific to write
#because your programs are too simple at this point, just add your name and
#the current date at the top of each program file. Then write one sentence
#describing what the program does.

# Author: [Numesh]
# Date: [20-03-2025]
# This program stores and prints the user's favorite number.

# Store favorite number in a variable
favorite_number = 7

# Create a message revealing the favorite number
message = f"My favorite number is {favorite_number}."

# Print the message
print(message)

--------------------------------------------------------------------------------------
#2-11. Zen of Python: Enter import this into a Python terminal session and skim
#through the additional principles.

import this
