from authors.model import Author
from utils import utils

def get_authors():
    authors = Author.objects.get_all()
    result = utils.deserializer(authors, many=True)
    return result

def create_author(data: Author):
    author = Author.objects.create(data)
    return utils.deserializer(author)

def get_author(id):
    author = Author.objects.get(id)
    return utils.deserializer(author)

def update_author(id, data):
    author = Author.objects.update(id,data)
    return utils.deserializer(author)

def delete_author(id, data):
    Author.objects.delete(id)
    return {"deleted": True}