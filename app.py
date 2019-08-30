from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from main.forms import SearchForm
import os
from models import Book, db

app = Flask(__name__)
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.shell_context_processor
def make_shell_content():
    return dict(db=db, Book=Book)


@app.route('/', methods=['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        book = Book.query.filter_by(book=form.book.data).first()
        if book is None:
            book = Book(book=form.book.data) # 待修改，从爬虫结果获取
            db.session.add(book)
            db.session.commit()


    return render_template('index.html', form=form)

@app.route('/upload')
def upload():
     render_template('upload.html')

