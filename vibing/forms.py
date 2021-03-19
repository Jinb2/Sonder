from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GenreForm(FlaskForm):

    genre = StringField('', validators=[DataRequired()])

    submit = SubmitField('Get recommendations')
