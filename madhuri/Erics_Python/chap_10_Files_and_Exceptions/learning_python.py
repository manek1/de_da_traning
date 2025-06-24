#10-1. Learning Python: Open a blank file in your text editor and write a few
#lines summarizing what you’ve learned about Python so far. Start each line
#with the phrase In Python you can.... Save the file as learning_python.txt in the
#same directory as your exercises from this chapter. Write a program that reads
#the file and prints what you wrote three times. Print the contents once by reading
#in the entire file, once by looping over the file object, and once by storing
#the lines in a list and then working with them outside the with block.


# File: read_learning_python.py

filename = "learning_python.txt"

# 1. Read and print the entire file
print("Reading entire file:\n")
with open(filename) as file:
    content = file.read()
    print(content)

# 2. Loop over the file object
print("\nReading line by line:\n")
with open(filename) as file:
    for line in file:
        print(line.strip())

# 3. Store lines in a list and work with them outside the with block
print("\nReading lines into a list:\n")
with open(filename) as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
