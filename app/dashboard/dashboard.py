from flask import Blueprint, render_template, flash, redirect, url_for, request
from typing import Dict
from app.dashboard.models.post import Post
from app.dashboard.models.category import Category
from app.auth.models.User import User
from app.dashboard.forms.post_form import PostForm


# from app.auth.models.User import User, Role
dashboard_bp = Blueprint('dashboard', __name__,
                         url_prefix="/dashboard", template_folder="templates")


@dashboard_bp.route('/')
def index():
    return render_template("dashboard.html")


from app.dashboard.models.post import Post


# dashboard = Blueprint('dashboard', __name__,
#                       url_prefix="/dashboard", template_folder="templates")


# GET ALL THE POSTS
@dashboard_bp.route('/posts/')
def get_posts():
    posts = Post.query.all()
    return render_template("posts/list.html", posts=posts)


# CREATE A NEW POST
@dashboard_bp.route('/create-post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    print("Here = ", form.publish.data)
    if form.validate_on_submit():
        print(form.title.data, form.category.data, form.description.data)
        post = Post(title=form.title.data, description=form.description.data,
                    category=form.category.data, source=form.source.data, publish=form.publish.data)
        post.save()
        flash("Post Created Successfully", "is-success")
        return redirect(url_for("dashboard.posts"))
    return render_template('posts/create_update.html', title="Create Post", form=form)


# DELETE A POST
@dashboard_bp.route("/posts/<int:id>/delete")
def delete_post(id):
    # Get post with the id
    post = Post.query.get_or_404(id)
    # Check if the user has permission to delete
    if post:
        post.delete()
        flash(f"{post.title} deleted successfully", "is-success")
        return redirect(url_for('dashboard.posts'))
    return render_template("posts/list.html")


@dashboard_bp.route('/posts/<int:id>/update', methods=['GET', 'POST'])
def update_post(id):
    # Get id of the post to update
    post = Post.query.get_or_404(id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        post.category = form.category.data
        post.source = form.source.data
        post.publish = form.publish.data
        post.update()
        flash("Post updated successfully", "is-success")
        return redirect(url_for('dashboard.posts'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.description.data = post.description
        form.category.data = post.category
        form.source.data = post.source
        form.publish.data = post.publish
    return render_template("posts/create_update.html", title="Update Post", form=form)


@dashboard_bp.route("/create-user", methods=['POST', 'GET'])
def create_user():
    return render_template("users/create_user.html")
# admin = Admin(app, name="News Summarizer", template_mode="bootstrap4")
# admin.add_view(ModelView(Category, db.session))
# admin.add_view(ModelView(Post, db.session))
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Role, db.session))


@dashboard_bp.route('/create-category', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        if request.form:
            name = request.form.get('name')
            description = request.form.get("description")
            category = Category(name=name, description=description)
            category.save()
            flash("Category Created Successfully", "is-success")
            return redirect(url_for("dashboard.categories"))

    return render_template('categories/create_update.html')


@dashboard_bp.route('/categories')
def get_categories():
    categories = Category.query.all()
    return render_template("categories/list.html", categories=categories)
