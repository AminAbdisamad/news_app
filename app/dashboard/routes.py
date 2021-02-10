from flask import Blueprint
from typing import Dict
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models.post import Post
from app.models.category import Category
from app.auth.models import User, Role
dashboard = Blueprint('dashboard', __name__, url_prefix="/dashboard")


@dashboard.route('/')
def index() -> Dict:
    return {"Route": "Dashboard Index"}


admin = Admin(app, name="News Summarizer", template_mode="bootstrap4")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
