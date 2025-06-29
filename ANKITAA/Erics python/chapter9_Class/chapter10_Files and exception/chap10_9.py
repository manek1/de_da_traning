#10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
#silently if either file is missing
def read_and_print(filename):
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        # Fail silently - do nothing if file is missing
        pass

files = ['cats.txt', 'dogs.txt']

for filename in files:
    read_and_print(filename)