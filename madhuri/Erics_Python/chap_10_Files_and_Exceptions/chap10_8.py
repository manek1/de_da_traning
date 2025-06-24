#10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
#names of cats in the first file and three names of dogs in the second file. Write
#a program that tries to read these files and print the contents of the file to the
#screen. Wrap your code in a try-except block to catch the FileNotFound error,
#and print a friendly message if a file is missing. Move one of the files to a different
#location on your system, and make sure the code in the except block
#executes properly.

def read_and_print(filename):
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found. Please check the file location.")

# List of files to read
files = ['cats.txt', 'dogs.txt']

for filename in files:
    read_and_print(filename)
