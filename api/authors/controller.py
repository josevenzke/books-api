from api.config.app import app, response
from api.authors import services

@app.route("/author")
class AuthorsResource:
    def get(self, req):
        authors = services.get_authors()
        return {"authors":authors}, 200
    
    def post(self,req):
        new_author = services.create_author(req.json)
        return {"author":new_author}, 201