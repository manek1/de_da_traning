#9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
#used a standard dictionary to represent a glossary. Rewrite the program using
#the OrderedDict class and make sure the order of the output matches the order
#in which key-value pairs were added to the dictionary.

from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'A reserved memory location to store values.'
glossary['loop'] = 'A sequence of instructions that is continually repeated.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['function'] = 'A block of organized, reusable code.'

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")
