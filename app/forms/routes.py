from flask import Blueprint, render_template, request
from app.models.post import Post
from app.models.category import Category
forms = Blueprint('forms', __name__, template_folder="templates", url_prefix="/forms",
                  static_folder="static", static_url_path='/static/site')


@forms.route("/", methods=['GET', 'POST'])
def index() -> str:
    # Get List of categories
    categories = Category.query.all()
    print(request.user_agent)

    if request.method == 'POST':
        print(dir(request))
        if request.form:
            title = request.form['title']
            description = request.form.get('description')
            source = request.form.get('source')
            category = request.form.get("category")
            print(category)
            post = Post(title=title, description=description,
                        source=source, categories=category)
            post.save()

            # print(title, description, source)
    return render_template("form.html", categories=categories)
