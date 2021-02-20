from flask import Blueprint, render_template, request, flash, url_for
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from werkzeug.utils import redirect
from flask_security.utils import hash_password
from app.auth.models.User import User, Role
from app import db, app
# Blue print for Auth
auth = Blueprint("auth", __name__, url_prefix="/auth",
                 template_folder="templates")

# Flask security setup
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)

# Create a user to test with


@app.before_first_request
def create_user():
    db.create_all()
    # user_datastore.create_user(email='matt@nobien.net', password='password')
    # db.session.commit()


# @login_required
@auth.route("/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        # if email exist and password login
        # email = User.query.filter_by(email=email).first()
        # password = User.query.filter_by(password=password).first()
        if email and password:
            redirect("/admin")
            flash("Logged in successfully")
        return redirect("/auth")
    return render_template("auth.html")


@auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        # email = request.data['email']
        # password = request.data['password']
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            # user = User(email=email, password=hash_password(password))
            print(email, password)
            # user.save()
            flash("User saved successfully")
            redirect(url_for('auth.login'))
    return render_template("register.html")
