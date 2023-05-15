from api.config.app import app, Response
from api.books import services

@app.route("/books")
class Books:
    def get(self, request):
        books = services.get_books()
        return Response(json={"books":books},status=200)
    
    def post(self, request):
        new_book = services.create_book(request.json)
        return Response(json={"book":new_book}, status=201)

@app.route("/books/{id}")
class Book:
    def get(self, request, id):
        book = services.get_book(id)
        return Response(json=book,status=200)

    def put(self, request, id):
        book = services.update_book(id, request.json)
        return Response(json=book,status=200)
    
    def delete(self, request, id):
        result = services.delete_book(id)
        return Response(json=result, status=200)