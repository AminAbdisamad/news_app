from flask import Blueprint, render_template, request, flash, url_for, redirect
import flask
from app.auth.models.User import User, Role
from app.auth.forms import LoginForm, RegisterForm
from app.dashboard.dashboard import dashboard_bp
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
    return render_template("login.html", form=form)


@auth_bp.route("/register/", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        register = User(username=form.username.data, email=form.email.data,
                        name=form.name.data, password=form.password.data)
        register.save()
        flash("Account Created", "is-success")
        redirect(url_for('auth.login'))
    return render_template("register.html", form=form)


@dashboard_bp.route("/create-user/", methods=["POST", "GET"])
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        register = User(username=form.username.data, email=form.email.data,
                        name=form.name.data, password=form.password.data)
        register.save()
        flash("Account Created", "is-success")
        redirect(url_for('dashboard.index'))
    return render_template("users/admin_create_user.html", form=form, title="Create User")


@dashboard_bp.route("/users/", methods=["GET"])
def get_users():
    users = User.query.all()
    for user in users:
        print(user.username)
    print(users)
    return render_template("users/list.html", users=users)


@dashboard_bp.route("/users/<int:id>/delete")
def delete_user(id):
    pass


@dashboard_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
def update_user(id):
    pass
