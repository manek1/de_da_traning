from book_module import Book
class Library:
    '''To create a collection of books and manage them'''
    def __init__(self):
                self.book_Collection=[]

    def add_book(self,book):
        self.book_Collection.append(book)
        print("The book "+book.title+" has been added to the book collection")

    def borrow_book(self,title):
        for book in self.book_Collection:
            if title.lower()==book.title.lower():
                if book.is_available():
                    book.available_copies=(book.available_copies -1)
                    print("The book '"+title.title()+"' has been borrowed.")
                    print('Available copies of the book have been updated to :' + str(book.available_copies))
                    book.display_info()
                    return
                else:
                    print("Currently we do not have enough copies of the book "+title.title())
                    return
        #This part takes care of the condition when borrowing a book which is not available in the library
        print("The book '"+title.title()+"' is not present in the Library. Please drop a suggestion to add the book into the Library.")


    def return_book(self,book_to_be_returned):
        for book in self.book_Collection:
            if book_to_be_returned.lower()==book.title.lower():
                book.display_info()
                book.available_copies=(book.available_copies +1)
                print("The book '"+book_to_be_returned.title()+"' has been returned.")
                book.display_info()
                return
               # This part takes care of the condition when returning a book which is not available in the library
        print("The book '"+book_to_be_returned.title()+"' is not part of the library and hence cannot be accepted for return.")


    def display_book(self):
        for book in self.book_Collection:
            print("=================================")
            book.display_info()





