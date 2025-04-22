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
    def __init__(self,title, author, ISBN, available_copies):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.available_copies=available_copies

    def display_info(self):
        print("The details of the book are as follows:  "+self.title+'\n'+self.author+'\n'+self.ISBN+'\n')

    def is_available(self):
        if int(self.available_copies) > 0:
            print('We do have copies of the book '+self.title+' available.')
        else:
            print("Sorry! There are  no copies available currently")

my_book=Book('Wings of Fire','APJ Kalam Sir','123','5')
my_book.display_info()
my_book.is_available()







