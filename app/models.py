from flask_sqlalchemy import SQLAlchemy
from config import Config

# import app

# db = SQLAlchemy(app)
# 这里定义db有问题，首先db已经在__init__.py里面定义了，
# 所以整个项目都应该用那个db实例，不应该重新定义，所以这一行是错误的。
# 这里用到的app也没有必要引入，所以注释掉。
# 按照下面这种方式引入
from . import db

ALLOWED_EXTENTIONS = {'txt', 'pdf', 'mobi', 'epub'}

class Book(db.Model):  # 这里需要用到db没有错
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    pub_date = db.Column(db.Integer)
    size = db.Column(db.Integer)
    introductions = db.Column(db.Text)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS