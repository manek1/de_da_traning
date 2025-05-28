#9-15. Python Module of the Week: One excellent resource for exploring the
#Python standard library is a site called Python Module of the Week. Go to
#http://pymotw.com/ and look at the table of contents. Find a module that
#looks interesting to you and read about it, or explore the documentation of
#the collections and random modules.

from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = Counter(words)
print(word_count)
