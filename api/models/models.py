from venSQL import Controller, BaseModel, validate_fields
from api.utils.constants import DB_SETTINGS

Controller.connect(database_settings=DB_SETTINGS)

@validate_fields
class Book(BaseModel):
    table_name = "books"
    name: str
    lenght: int
    genre: str
