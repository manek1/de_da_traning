#10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
#and find a few texts you’d like to analyze. Download the text files for these
#works, or copy the raw text from your browser into a text file on your
#computer.
#You can use the count() method to find out how many times a word or
#phrase appears in a string. For example, the following code counts the number
#of times 'row' appears in a string:
#>>> line = "Row, row, row your boat"
#>>> line.count('row')
#2
#>>> line.lower().count('row')
#3
#Notice that converting the string to lowercase using lower() catches
#all appearances of the word you’re looking for, regardless of how it’s
#formatted.
#Write a program that reads the files you found at Project Gutenberg and
#determines how many times the word 'the' appears in each text.

def count_the(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return

    # Count occurrences of 'the' as a substring
    # This counts all occurrences, but it might count parts of other words (like 'there').
    the_count = text.count('the')

    print(f"The word 'the' appears {the_count} times in {filename}.")

# List of your downloaded files from Project Gutenberg
files = ['pride_and_prejudice.txt', 'moby_dick.txt']  # Replace with your actual filenames

for file in files:
    count_the(file)
