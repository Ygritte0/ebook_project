from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    search = StringField('Search Book', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Search')