from api.config.app import app, response
from api.authors import services

@app.route("/book")
class AuthorsResource:
    def get(self, req):
        authors = services.get_authors()
        response.json = {"authors":authors}
        return response
    
    def post(self,req):
        print(req.json)
        new_author = services.create_author(req.json)
        response.json = req.json
        return response