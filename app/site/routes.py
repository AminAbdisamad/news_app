from flask import Blueprint, render_template
from app.models.post import Post
from app.models.category import Category


site = Blueprint('site', __name__, template_folder="templates",
                 static_folder="static", static_url_path='/static/site')


@site.route("/")
def index() -> str:
    # Get Data from database
    posts = Post.query.all()
    categories = Category.query.all()
    # posts_by_category = Post.query.filter(
    #     Post.categories.name == Category.name)
    for post in posts:
        print(post.categories)
        # posts_by_category = Post.query.filter(
        #     post.categories == Category.name)
        # print(posts_by_category)
    return render_template("site.html", posts=posts, categories=categories)
