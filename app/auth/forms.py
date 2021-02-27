from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, RadioField
from wtforms.validators import Length, DataRequired, email_validator

# from wtforms_sqlalchemy.fields import


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(), Length(min=3, max=30)], render_kw={"placeholder": "Your Name"})
    username = StringField("Username", validators=[DataRequired(),
                                                   Length(min=3, max=10)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired()], render_kw={
                        "placeholder": "geedi@example.com"})
    password = StringField("Password", validators=[
        DataRequired(), Length(min=6, max=50)], render_kw={
        "placeholder": "*********"})

    submit = SubmitField("Create")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={
                        "placeholder": "geedi@example.com"})
    password = StringField("Password", validators=[
        DataRequired(), Length(min=6, max=50)], render_kw={
        "placeholder": "*********"})
    submit = SubmitField("Login")
