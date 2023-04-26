from venzpy import Venzpy, Response
from venSQL import Controller
from api.utils.constants import DB_SETTINGS


Controller.connect(database_settings=DB_SETTINGS)
app = Venzpy()

