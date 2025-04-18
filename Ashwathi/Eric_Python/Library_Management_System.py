'''You are building a simple Library Management System. It should be able to:
	•	Store details about books (title, author, ISBN, available copies)
	•	Allow users to borrow and return books
	•	Display available books
'''
'''Instructions
Split the code into 2 modules:
Module 1: book.py
This will have the Book class with:
	•	_init_: to initialize book details
	•	display_info(): to print book details
	•	is_available(): to check if copies are available
'''
class Book():
    def __init__(self,title, author, ISBN, available copies):
        self.title = title
        self.author = author
