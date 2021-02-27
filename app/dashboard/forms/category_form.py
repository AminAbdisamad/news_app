from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, length


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), length(min=3, max=20)])
    description = TextAreaField('Description')
    submit = SubmitField("Submit")
