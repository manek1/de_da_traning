from book_module import Book
from library_module import Library

book1=Book('Wings of Fire','APJ Kalam Sir','123',0)
book2=Book('Atomic Habits','JAmes Clear','456',10)
book3=Book('Norwegian Wood','Murakami','789',10)

my_lib=Library()

print('\n Adding books: \n')
my_lib.add_book(book1)
my_lib.add_book(book2)
my_lib.add_book(book3)
print('-----------------------------------------------------------')
print('\n Borrowing a book:')

#Borrowing a book present in library
my_lib.borrow_book('Norwegian Wood')
#Borrowing a book that has 0 available copies
my_lib.borrow_book('Wings of Fire')
#Borrowing a book that is not part of the library
my_lib.borrow_book('Utopia')

print('----------------------------------------------------')
print('\nReturning a book: \n')
#Returning a book present in the library
my_lib.return_book('Atomic Habits')
#Returning a book not part of the library
my_lib.return_book('Utopia')



