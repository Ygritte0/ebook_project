from flask import Flask, render_template, flash
from .main.forms import SearchForm
from .models import Book
from flask_sqlalchemy import BaseQuery

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    book = Book.query.filter_by(book=form.book.data).all()
    if book is None:
        return flash('This book does not exits.')
    else:
        pass

    return render_template('index.html')

@app.route('/upload-books')
def upload():

    render_template('upload.html')

