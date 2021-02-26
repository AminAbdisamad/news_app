from flask import Blueprint, render_template
from app.dashboard.models.post import Post
from app.dashboard.models.category import Category


site = Blueprint('site', __name__, template_folder="templates",
                 static_folder="static", static_url_path='/static/site')


@site.route("/")
def index() -> str:
    # Get Data from database
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template("site.html", posts=posts, categories=categories)
