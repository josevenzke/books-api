from api.config.app import app, Response
from api.authors import services

@app.route(path="/authors", methods=['GET'])
def get_all(request):
    authors = services.get_authors()
    return Response(json={'authors':authors}, status=200)


@app.route(path="/authors", methods=['POST'])
def create(request):
    new_author = services.create_author(request.json)
    return Response(json={"author":new_author}, status=201)

@app.route(path="/authors/{id}", methods=['GET'])
def get_one(request, id):
    author = services.get_author(id)
    return Response(json={'author':author}, status=200)

@app.route(path="/authors/{id}", methods=['PUT'])
def update(request, id):
    author = services.update_author(id)
    return Response(json={'author':author}, status=200)

@app.route(path="/authors/{id}", methods=['DELETE'])
def delete(request, id):
    result = services.delete_author(id)
    return Response(json=result, status=200)