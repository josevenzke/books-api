import json
from api.config.app import app, response
from api.books import services

@app.route("/book")
class BooksResource:
    def get(self, req):
        books = services.get_books()
        response.json = {"books":books}
        return response
    
    def post(self, request):
        data = request.json
        response.json = data
        return response
    

@app.route("/about",  methods=['GET','POST'])
def about(request):
    books_data = [
    {"name": "Pythoning", "lenght": 400, "genre": "tech"},
    {"name": "Harry Potter", "lenght": 400, "genre": "fantasy"}
    ]
    for book in books_data:
        x = Book.objects.create(object=book)

    response.text = "Hello from the ABOUT page"
    return response

@app.route("/about/{name}",  methods=['GET','POST'])
def about(request, name):
    response.text = f"Hello {name}"
    return response
