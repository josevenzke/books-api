from api.authors.model import Author
from api.utils import utils

def get_authors():
    authors = Author.objects.get_all()
    result = utils.deserializer(authors)
    return result

def create_author(data: Author):
    author = Author.objects.create(data)
    return utils.deserializer([author])
