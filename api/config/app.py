from venzpy import Venzpy, response
from venSQL import Controller
from api.utils.constants import DB_SETTINGS


Controller.connect(database_settings=DB_SETTINGS)
app = Venzpy()

