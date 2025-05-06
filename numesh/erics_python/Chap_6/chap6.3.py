#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
#However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous
#chapters. Use these words as the keys in your glossary, and store their
#meanings as values.
#• Print each word and its meaning as neatly formatted output. You might
#print the word followed by a colon and then its meaning, or print the word
#on one line and then print its meaning indented on a second line. Use the
#newline character (\n) to insert a blank line between each word-meaning
#pair in your output.

# We create a dictionary called 'glossary' where:
# - Keys are programming terms (words).
# - Values are their meanings (definitions).

glossary = {
    'variable': 'A named location used to store data in a program.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'An ordered collection of items that can be changed (mutable).'
}

# We use a for loop to go through each word and its meaning.
for word, meaning in glossary.items():
    # Print the word followed by a colon
    print(f"{word}:\n{meaning}\n")
