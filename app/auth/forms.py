from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, RadioField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from app.auth.models.User import User

# from wtforms_sqlalchemy.fields import


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[
        DataRequired(message="Enter your name please"), Length(min=3, max=30)], render_kw={"placeholder": "Your Name"})
    username = StringField("Username", validators=[DataRequired(),
                                                   Length(min=3, max=10)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "geedi@example.com"})
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=5)], render_kw={
        "placeholder": "*********"})
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), Length(min=5), EqualTo('password', message="Confirm password must be equal to password")], render_kw={
        "placeholder": "*********"})

    submit = SubmitField("Create")

    def validate_username(self, username):
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError("Username is taken. come up with new one :)")

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email exist. try different one :)")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "geedi@example.com"})
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=6, max=50)], render_kw={
        "placeholder": "*********"})
    submit = SubmitField("Login")


class RolesForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired(), Length(min=3, max=20)])
    description = TextAreaField('Description')
    submit = SubmitField("Submit")
