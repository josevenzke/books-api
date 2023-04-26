from api.books.model import Book
from api.utils import utils

def get_books():
    books = Book.objects.get_all()
    return utils.deserializer(books, many=True)

def get_book(id):
    books = Book.objects.get(id)
    return utils.deserializer(books)

def create_book(data: dict):
    author = Book.objects.create(data)
    return utils.deserializer(author)
