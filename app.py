from flask import Flask, request, jsonify
from models import db, Book
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize Marshmallow with the Flask app
ma = Marshmallow(app)

@app.before_request
def create_tables():
    with app.app_context():
        db.create_all()
    
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        include_fk = True

# Single book schema
book_schema = BookSchema()
# Multiple books schema
books_schema = BookSchema(many=True)

# Create a Book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_date=data['published_date'],
        isbn=data['isbn'],
        page_count=data['page_count'],
        cover=data['cover'],
        language=data['language']
    )
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book), 201

# Get a Book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return book_schema.jsonify(book)

# Get Books with Filters
@app.route('/books', methods=['GET'])
def get_books():
    query_params = request.args
    filters = {}
    for param in ['author', 'published_date', 'language']:
        if query_params.get(param):
            filters[param] = query_params.get(param)

    books = Book.query.filter_by(**filters).all()
    return books_schema.jsonify(books)

# Update a Book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    book.title = data['title']
    book.author = data['author']
    book.published_date = data['published_date']
    book.isbn = data['isbn']
    book.page_count = data['page_count']
    book.cover = data['cover']
    book.language = data['language']

    db.session.commit()
    return book_schema.jsonify(book)

# Delete a Book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
