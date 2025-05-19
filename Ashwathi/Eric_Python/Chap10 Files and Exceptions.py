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

