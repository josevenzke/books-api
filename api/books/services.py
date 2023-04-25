from api.books.model import Book
from api.utils.utils import deserializer

def get_books():
    books = Book.objects.get_all()
    result = deserializer(books)
    return result
