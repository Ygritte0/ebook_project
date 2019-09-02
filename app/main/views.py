from flask import render_template,flash
from app import main
from .forms import SearchForm
from ..models import Book
from flask import render_template, flash
from flask_migrate import Migrate

from .forms import SearchForm





@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    # book = request.args.get('book', '')
    if form.validate_on_submit():
     book = Book.query.filter_by(book=form.book.data).all()
     if book is None:
         flash('We do not have, you can upload.')
         return render_template('index.html', form=form)
         # else:
         #     return flash('We do not have, you can upload.')


@main.route('/upload', methods=['GET', 'POST'])
def upload():

    return render_template('upload.html')

















