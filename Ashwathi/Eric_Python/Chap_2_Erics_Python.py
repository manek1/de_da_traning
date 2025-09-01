#Chap 2 contains variables, composing a message, namecases, use of quotes,tabs, newlines, stripping whitespaces, use of str, numeric operations and Zen of Python!

#2-1.  Simple Message:  Store a message in a variable, and then print that message
message="Hi! This is the first exercise in Erics Python!"
print(message)

#2-2.  Simple Messages:  Store a message in a variable, and print that message Then change the value of your variable to a new message, and print the new message
msg="The book was written in the era of Python 3.5 series"
print(msg)
msg="And today we have Python 3.13 series! We have come a long way!"
print(msg)

#2-3.  Personal Message:  Store a person’s name in a variable, and print a mes-sage to that person  Your message should be simple, such as, “Hello Eric,
#would you like to learn some Python today?”
name="Eric Matthews"
print("Hi!" + name.title() + ". I am loving your book!")

#2-4.  Name Cases: Store a person’s name in a variable, and then print that per-son’s name in lowercase, uppercase, and titlecase
name= "ada lOVElace"
print(name.upper())
print(name.lower())
print(name.title())

#2-5.  Famous Quote: Find a quote from a famous person you admire  Print the quote and the name of its author  Your output should look something like the
#following, including the quotation marks:
print('\tAndrew Kix promotes the idea that,"The secret about consistency is in turning the things\n\tyou hate doing, into things you do without thinking!"')

#2-6.  Famous Quote 2: Repeat Exercise 2-5, but this time store the famous per-son’s name in a variable called  famous_person Then compose your message and store it in a new variable called  message Print your message
famous_person="andrew Kix"
print('\t'+famous_person.title() + ' promotes the idea that,"The secret about consistency is in turning the things\n\tyou hate doing, into things you do without thinking!"')

#2-7.  Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name  Make sure you use each character combination, " \t" and " \n", at least once
name="     Aryaveer       "
print("Hi " +name+","+"\n\tI cannot wait to see you!")
print("Hi " +name.lstrip()+","+"\n\tI cannot wait to see you!")
print("Hi " +name.rstrip()+","+"\n\tI cannot wait to see you!")
print("Hi " +name.strip()+","+"\n\tI cannot wait to see you!")

#2-8.  Number Eight: Write addition, subtraction, multiplication, and division
#operations that each result in the number 8  Be sure to enclose your operations in  print statements to see the results  You should create four lines that look
#like this:

print(5+3)
print(16-8)
print(4*2)
print(32/4)

#2-9.  Favorite Number: Store your favorite number in a variable  Then, using that variable, create a message that reveals your favorite number  Print that message

fav_no = 9
print("Soooo, my fav no is:"+str(fav_no)+"!!")

#2-11.  Zen of Python: Enter i mport this into a Python terminal session and skim through the additional principles
import this