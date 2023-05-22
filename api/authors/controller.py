from config.app import app
from authors import services


@app.route(path="/authors", methods=['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        authors = services.get_authors()
        return {'authors':authors}, 200
    if request.method == 'POST':
        new_author = services.create_author(request.json)
        return {"author":new_author}, 201

@app.route(path="/authors/{id}", methods=['GET', 'PUT','DELETE'])
def book(request, id):
    if request.method == 'GET':
        author = services.get_author(id)
        return {'author':author}, 200
    if request.method == 'PUT':
        author = services.update_author(id, request.json)
        return {'author':author},200
    if request.method == 'DELETE':
        result = services.delete_author(id)
        return result, 200
