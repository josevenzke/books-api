from venzpy import Venzpy, response
from models import Book
from utils import deserializer

app = Venzpy()

@app.route("/books", methods=['GET','POST'])
def home(request):
    if request.method == 'GET':
        books = Book.objects.get_all()
        result = deserializer(books)
        response.json = {"books":result}

    elif request.method == 'POST':
        books_data = [
            {"name": "Pythoning", "lenght": 400, "genre": "tech"},
            {"name": "Harry Potter", "lenght": 400, "genre": "fantasy"}
        ]
        for book in books_data:
            Book.objects.create(object=book)

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

@app.route("/book")
class BooksResource:
    def get(self, req):
        response.json = {"page":"Books Page"}
        return response
    
    def post(self,req):
        print(req.json)
        response.json = req.json
        return response