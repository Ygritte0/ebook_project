from flask_sqlalchemy import SQLAlchemy
import app


db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    size = db.Column(db.Integer)
    introductions = db.Column(db.Text)


