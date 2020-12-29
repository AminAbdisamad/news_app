from flask import Blueprint,render_template
from app.models.post import Post
from app.models.category import Category



site = Blueprint('site',__name__,template_folder="templates")

@site.route("/")
def index()->str:
    # Get Data from database
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template("index.html",posts=posts,categories=categories)



