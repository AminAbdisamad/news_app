from flask import Blueprint,render_template
from app.site.models import Post



site = Blueprint('site',__name__,template_folder="templates")

@site.route("/")
def index()->str:
    # Get Data from database
    posts = Post.query.all()
    return render_template("index.html",posts=posts)



