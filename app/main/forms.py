from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, FloatField, FileField, DateField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    title = StringField('Search Book', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Search')

class UploadForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired(), Length(1, 100)] )
    author = StringField('Author', validators=[DataRequired(), Length(1, 64)])
    pub_date = DateField('Publish Date')
    size = FloatField('Size')
    introductions = TextAreaField('Introductions')
    file = FileField('Choose file')
    submit = SubmitField('Upload')