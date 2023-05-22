from books.model import Book
from utils import utils

def get_books():
    books = Book.objects.get_all()
    return utils.deserializer(books, many=True)

def get_book(id):
    books = Book.objects.get(id)
    return utils.deserializer(books)

def create_book(data: dict):
    book = Book(**data)
    book.save()
    return utils.deserializer(book)

def update_book(id: int, data: dict) -> dict:
    book = Book.objects.get(id)
    for key in data.keys():
        setattr(book, key, data[key])
    book.save()
    return utils.deserializer(book)

def delete_book(id: int):
    Book.objects.delete(id)
    return {"deleted":True}