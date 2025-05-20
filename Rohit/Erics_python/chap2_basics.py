"""Cha - 2 VARIABLES AND SIMPLE DATA TYPES (EX:- variable,strings,numbers,comment and the zen of python)"""
"""2-1. Simple Message: Store a message in a variable, and then print that
message."""

message = "Hello, this is my first python message!"
print(message)

"""2-2. Simple Messages: Store a message in a variable, and print that message.
Then change the value of your variable to a new message, and print the new
message."""

message = "Hello, this is my second python message!"
print(message)

new_message = "Hello, this is my third python message!"
print(new_message)


"""2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”"""

name = "Eric Matthews"
print("Hello" + name.title() + ",would you like to learn some python today?")

"""2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase,
 uppercase, and titlecase."""

name = "ada lovelace"
print(name.lower())
print(name.upper())
print(name.title())

"""2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
"""
print('\tAlbert Einstein once said,"A person who never made a mistake never tried anything new."')

"""2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message
and store it in a new variable called message. Print your message"""

famous_person = "Albert Einstein"
message = ('\t' + famous_person.title() + 'Albert Einstein once said,"A person who never made a mistake never tried anything new."')
print(message)

"""2-7. Stripping Names: Store a person’s name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip()."""

name = "     ROHIT SHARMA     "
print("The GOAT" +name+","+"\n\tAnnounced his T20 retirement last year AND NOW from TEST CRICKET...G.O.A.T OPENER")
print("The GOAT" +name.lstrip()+","+"\n\tAnnounced his T20 retirement last year AND NOW from TEST CRICKET...G.O.A.T OPENER")
print("The GOAT" +name.rstrip()+","+"\n\tAnnounced his T20 retirement last year AND NOW from TEST CRICKET...G.O.A.T OPENER")
print("The GOAT" +name.strip()+","+"\n\tAnnounced his T20 retirement last year AND NOW from TEST CRICKET...G.O.A.T OPENER")

"""2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print statements to see the results. You should create four lines that look """

print(5+3)
print(16-8)
print(4*2)
print(32/4)

"""2-9. Favorite Number: Store your favorite number in a variable. Then, using
that variable, create a message that reveals your favorite number. Print that
message"""

fvt_no = 45
print("My favorite is-" +str(fvt_no) +" " "because this is ROHIT SHARMA Jeasy number")