from flask import Blueprint, render_template, request, redirect, flash
from typing import Dict
from flask.helpers import url_for
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.dashboard.models.post import Post
from app.dashboard.models.category import Category
from app.auth.models.User import User
from app.dashboard.forms.post_form import PostForm
# from app.auth.models.User import User, Role
dashboard = Blueprint('dashboard', __name__,
                      url_prefix="/dashboard", template_folder="templates")


@dashboard.route('/')
def index():
    return render_template("dashboard.html")


# POSTS - Make sure to put here otherwise there will be circular import
from app.dashboard.views import posts


@dashboard.route('/create-category', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        if request.form:
            name = request.form.get('name')
            description = request.form.get("description")
            category = Category(name=name, description=description)
            category.save()
            flash("Category Created Successfully", "is-success")
            return redirect(url_for("dashboard.categories"))

    return render_template('categories/create_category.html')


@dashboard.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template("categories/categories.html", categories=categories)


@dashboard.route("/users")
def users():
    users = User.query.all()
    return render_template("users/users.html")


@dashboard.route("/create-user", methods=['POST', 'GET'])
def create_user():
    return render_template("users/create_user.html")
# admin = Admin(app, name="News Summarizer", template_mode="bootstrap4")
# admin.add_view(ModelView(Category, db.session))
# admin.add_view(ModelView(Post, db.session))
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Role, db.session))
