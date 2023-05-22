from venzpy import Venzpy, Response
from venSQL import Controller
from utils.constants import DB_SETTINGS
from books.model import Book

Controller.connect(database_settings=DB_SETTINGS)
x = Controller(Book).get_all()
print(x)
print(Controller.connection)
app = Venzpy()

from authors import controller
from books import controller