from api.authors.model import Author
from api.utils.utils import deserializer

def get_authors():
    authors = Author.objects.get_all()
    result = deserializer(authors)
    return result
