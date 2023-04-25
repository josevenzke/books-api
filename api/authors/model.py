from venSQL import BaseModel, validate_fields
from api.utils.constants import DB_SETTINGS

@validate_fields
class Author(BaseModel):
    table_name = "authors"
    name: str
    age: int
