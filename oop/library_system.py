class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
class EBook(Book):
  def __init__(self, title, author, file_size):
    super()__init__(title, author)
    self.file_size = file_size
class PrintBook(Book):
  super()__init__(title, author)
  def __init__(self, title, authorpage_count):
    self.page_count = page_count
class (Library):
  def __init__(self, books):
    self.books = books[]
    def add_book(self, book):
      books.append(Book, Ebook, PrintBook)
    def list_books(self):
      print(Library())
