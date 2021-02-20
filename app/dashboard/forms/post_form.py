from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Length, DataRequired
from app.dashboard.models.category import Category
# from wtforms_sqlalchemy.fields import


class PostForm(FlaskForm):
    title = StringField("Title", validators=[
                        DataRequired(), Length(min=3, max=20)])
    description = TextAreaField("Description", validators=[
                                DataRequired(), Length(max=1500)])
    category = SelectField('Category', choices=[Category.name])
    source = StringField("Source", validators=[
                         DataRequired(), Length(min=3, max=20)])
    submit = SubmitField("Create")
