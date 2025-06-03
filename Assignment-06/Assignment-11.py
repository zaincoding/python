
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
         cls.total_books +=1

    def __init__(self, title, author):
         self.title = title
         self.author = author
         Book.increment_book_count()
     
         
book = Book('Mountain Snow', 'zain')
book1 = Book('Blue Hill', 'TK.Khan')



print(book1.total_books)
