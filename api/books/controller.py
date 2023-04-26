import json
from api.config.app import app, Response
from api.books import services

@app.route("/book")
class Books:
    def get(self, request):
        books = services.get_books()
        return Response(json={"books":books},status=200)
    
    def post(self, request):
        new_book = services.create_book(request.json)
        return Response(json={"book":new_book}, status=201)

@app.route("/book/{id}")
class Book:
    def get(self, request, id):
        book = services.get_book(id)
        return Response(json=book,status=200)
    
    def post(self, request):
        new_book = services.create_book(request.json)
        return Response(json={"book":new_book}, status=201)