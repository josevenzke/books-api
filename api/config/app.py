from venzpy import Venzpy, Response
from venSQL import Controller
from utils.constants import DB_SETTINGS
from books.model import Book

Controller.connect(database_settings=DB_SETTINGS)
app = Venzpy()

from authors import controller
from books import controller