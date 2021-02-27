from flask import Blueprint, render_template, request, flash, url_for, redirect
import flask
from app.auth.models.User import User, Role
from app.auth.forms import LoginForm, RegisterForm
# Blue print for Auth
auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                    template_folder="templates")


@auth_bp.route("/", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data()
        password = form.password.data()
        print(email, password)
        # if email exist and password login
        # email = User.query.filter_by(email=email).first()
        # password = User.query.filter_by(password=password).first()
        if email and password:
            redirect("/dashboard")
            flash("Logged in successfully")
        return redirect("/auth")
    return render_template("auth.html", form=form)


@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        register = User(username=form.username, email=form.email,
                        name=form.name, password=form.password)
        register.save()
        flash("Account Created", "is-success")
        redirect(url_for('auth.login'))
    return render_template("register.html", form=form)
