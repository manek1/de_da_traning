class Book:
    '''Deals with books'''
    def __init__(self,title, author, ISBN, available_copies):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.available_copies=available_copies

    def display_info(self):
        '''Displays the details of the book'''
        print("The details of the book are as follows: \n\t"
              "Book's Title: "+self.title.title()+
              "\n\tAuthor: "+self.author.title()+
              "\n\tISBN: "+self.ISBN+
              "\n\tAvailable copies of the book: "+str(self.available_copies))

    def is_available(self):
        if int(self.available_copies)>0:
            print("\nThe book, "+self.title.title()+" is available. No of copies available are : "+str(self.available_copies))
            return int(self.available_copies)>0
        else:
            print("Sorry! The book, "+self.title.title()+" is not available.")



