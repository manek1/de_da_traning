#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

# Define a dictionary called 'glossary' with 10 programming terms and their definitions
glossary = {
    'variable': 'A named location used to store data in a program.',
    'function': 'A block of reusable code that performs a specific task.',
    'loop': 'A control structure used to repeat a block of code multiple times.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'list': 'An ordered collection of items that can be changed (mutable).',
    'tuple': 'An ordered, immutable collection of items.',
    'boolean': 'A data type that can have one of two values: True or False.',
    'if statement': 'A control structure that allows conditional execution of code.',
    'import': 'Used to include external modules or libraries into your program.',
    'comment': 'Text in the code that is ignored by the interpreter, used for notes.'
}

# Loop through the dictionary using a for loop
for word, meaning in glossary.items():
    # Print the word and its meaning, formatted with a newline and indentation
    print(f"{word}:\n  {meaning}\n")