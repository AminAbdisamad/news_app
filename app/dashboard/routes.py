from flask import Blueprint
from typing import Dict
dashboard = Blueprint('dashboard',__name__,url_prefix="/dashboard")

@dashboard.route('/')
def index() ->Dict:
    return {"Route":"Dashboard Index"}

