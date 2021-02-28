from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user, login_user
from flask_login.utils import logout_user
from app.auth.models.User import User, Role
from app.auth.forms import LoginForm, RegisterForm, RolesForm
from app.dashboard.dashboard import dashboard_bp
from app import bcrypt
# Blue print for Auth
auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                    template_folder="templates")


@auth_bp.route("/", methods=["POST", "GET"])
def login():
    # chekc if user is already logged in
    # TODO1: also implement checking if admin/staff
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    if form.validate_on_submit():
        # Check if email exist in db
        # check if email and password match
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # User is logged in
            login_user(user)  # Add to the session that user is logged in
            flash("Logged in successfully", "is-success")
            return redirect(url_for("dashboard.index"))

        else:
            flash("Invalid credentials", "is-danger")
            redirect(url_for("auth.login"))
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Successfully logout", "is-success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/register/", methods=["POST", "GET"])
def register():
    # If user is already logged in we need to redirect to dashboard
    # TODO1: also implement checking if admin/staff
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        register = User(username=form.username.data, email=form.email.data,
                        name=form.name.data, password=hashed_password)
        register.save()
        flash("Account Created", "is-success")
        return redirect(url_for('auth.login'))
    return render_template("register.html", form=form)


@dashboard_bp.route("/users/create/", methods=["POST", "GET"])
def create_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    name=form.name.data, password=form.password.data)
        user.save()
        flash("Account Created", "is-success")
        return redirect(url_for('dashboard.get_users'))
    return render_template("users/admin_create_user.html", form=form, title="Create User")


@dashboard_bp.route("/users/", methods=["GET"])
def get_users():
    users = User.query.all()
    return render_template("users/list.html", users=users)


@dashboard_bp.route("/users/<int:id>/delete")
def delete_user(id):
    pass


@dashboard_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
def update_user(id):
    pass


@dashboard_bp.route("/roles/")
def get_roles():
    roles = Role.query.all()
    return render_template("users/role_list.html", roles=roles)


@dashboard_bp.route("/roles/create", methods=['GET', 'POST'])
def create_roles():
    form = RolesForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data, description=form.description.data)
        role.save()
        flash("Role Created", "is-success")
        return redirect(url_for('dashboard.get_roles'))
    return render_template("users/create_update_role.html", form=form)


@dashboard_bp.route("/roles/<int:id>/delete")
def delete_role(id):
    pass


@dashboard_bp.route("/roles/<int:id>/update", methods=["GET", "POST"])
def update_role(id):
    pass
