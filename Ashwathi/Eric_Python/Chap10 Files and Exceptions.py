'''Reading entire contents of file at once

with open ('Chap10_pi_digits') as file_object:
    contents=file_object.read()
    print(contents)
'''
'''Reading line by line

with open('Chap10_pi_digits') as file_objects:
    for line in file_objects:
        print(line)'''
'''Working with file contents'''
'''
file_name='Chap10_pi_digits'
with open(file_name) as file_object:
    lines=file_object.readlines()
    py_string=''
    for line in lines:
        py_string+=line.strip()
print(py_string)
print(len(py_string))
'''

'''10-1. Learning Python: Open a blank file in your text editor and write a few 
lines summarizing what you’ve learned about Python so far. Start each line 
with the phrase In Python you can.... Save the file as learning_python.txt in the 
same directory as your exercises from this chapter. Write a program that reads 
the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing 
the lines in a list and then working with them outside the with block.'''

''' Reading the entire file 
with open ('Chap10_Ex1_learning_python') as file_object:
    content=file_object.read()
    print(content)
    print(content)
    print(content)
'''
'''Reading by looping over file objects
with open('Chap10_Ex1_learning_python') as file_objects:
    for line in file_objects:
        print(line)
'''
'''Storing file contents in list and working outside with block'''


'''10-2. Learning C:Read in each line from the file you just created, learning_python.txt, and 
replace the word Python with the name of another language, such as C. Print 
each modified line to the screen.'''
'''
with open('Chap10_Ex1_learning_python') as file_object:
    lines=file_object.read()
    modified_line=lines.replace('python','C')
    print(modified_line)
'''
'''10-3. Guest: Write a program that prompts the user for their name. When they 
respond, write their name to a file called guest.txt.'''
'''
with open ('Guest','a') as file:
    while True:
        name=input("Please enter your name or type quit to exit : ")
        if name.lower()=='quit':
            break
        else:
            file.write(name+'\n')
'''
'''10-4. Guest Book: Write a while loop that prompts users for their name. When 
they enter their name, print a greeting to the screen and add a line recording 
their visit in a file called guest_book.txt. Make sure each entry appears on a 
new line in the file.'''


while True:
    name = input("Please enter your name or type quit to exit :")
    if name.lower()=='quit':
        break
    else:
        print("Hi "+name.title()+". Welcome !!!")
        with open ('Guest_book','a') as file:
            file.write(name+'\n')



