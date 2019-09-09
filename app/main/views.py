
# 如果是一般的模块引用，这么写是正确的绝对引用。
# 但是在这里不能这么写，要使用相对引用
# from app import main
import os
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
# from sqlalchemy.orm import create_session
from . import main
from .forms import SearchForm, UploadForm
from ..models import Book, allowed_file
from .. import db
from config import config
from app import create_app


@main.route('/', methods=['GET'])
def index():
    form = SearchForm()
    book = request.args.get('title', '')
    if book:
        print('request.args is:', request.args)
        books = Book.query.filter_by(title=book).order_by(Book.id).all()
    else:
        books = Book.query.order_by(Book.title).all()
    return render_template('index.html', form=form, books=books)


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        if 'file' not in request.files:
            flash('No file part.')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file.')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            book = Book(title=form.title.data, author=form.author.data,
                        pub_date=form.pub_date.data, size=form.size.data,
                        introductions=form.introductions.data)
            db.session.add(book)
            db.session.commit()
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('.upload', filename=filename))
    return render_template('upload.html', form=form)
    #     book = Book(title=form.title.data,
    #         author=form.author.data,
    #         size=form.size.data,
    #         pub_date=form.pub_date.data,
    #         introductions=form.introductions.data)
    #     db.session.add(book)
    #     db.session.commit()
    #     return redirect(url_for('.recommend'))






@main.route('/recommend',methods=['GET'])
def recommend():
    # db = get_db()
    results = []
    rows = Book.query.all()
    for row in rows:
        results.append(row)
    return render_template('recommend.html', results=results)
