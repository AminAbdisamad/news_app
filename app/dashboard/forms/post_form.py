from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, RadioField
from wtforms.validators import Length, DataRequired
from app.dashboard.models.category import Category
# from wtforms_sqlalchemy.fields import


class PostForm(FlaskForm):
    title = StringField("Title", validators=[
                        DataRequired(), Length(min=3, max=20)])
    description = TextAreaField("Description", validators=[
                                DataRequired(), Length(max=1500)])
    category = SelectField('Category', choices=[
                           category.name for category in Category.query.all()])

    source = StringField("Source", validators=[
                         DataRequired(), Length(min=3, max=20)])

    publish = RadioField(
        'Publish?',
        choices=[("yes", 'Yes'), ("no", 'No')], default="yes"
    )
    submit = SubmitField("Submit")


# ! To fix issue of select that's not updating use this code
 # category = SelectField("Category")
  # def __init__(self):
    #     super(PostForm, self).__init__()
    #     self.category.choices = [
    #         category.name for category in Category.query.all()]
