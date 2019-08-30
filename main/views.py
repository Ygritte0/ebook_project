from flask import render_template, url_for, Blueprint
import  main
from .forms import SearchForm

@main.route('/')
def index():
    form = SearchForm()
    return render_template('index.html', form=form)

@main.route('/upload')
def upload():
     render_template('upload.html')