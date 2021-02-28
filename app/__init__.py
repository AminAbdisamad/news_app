from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app import config

# from werkzeug import generate_password_hash,check_password_hash
app = Flask(__name__)

# ?We could directly add configs to app instance like this
# app.config["SECRET_KEY"] = "Imsecret"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ?Or Read from another class
# app.config.from_object(DevelopmentConfig)


if app.config["ENV"] == 'production':
    app.config.from_object(config.ProductionConfig)

    #  Display Errors nicely
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server(error):
        return render_template("500.html"), 500

elif app.config["ENV"] == 'testing':
    app.config.from_object(config.TestingConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

# To set envr
# export FLASK_ENV=production
# ? Extensions
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manger = LoginManager(app)


#  Errors
# @app.errorhandler(404)
# def not_found(error):
#     return render_template("404.html"), 404


# @app.errorhandler(500)
# def internal_server(error):
#     return render_template("500.html"), 500


@app.before_first_request
def create_db():
    # db.drop_all()
    db.create_all()


# Register Blueprints
from app.dashboard.dashboard import dashboard_bp
from app.site.routes import site
from app.auth.auth import auth_bp


app.register_blueprint(dashboard_bp)
app.register_blueprint(site)
app.register_blueprint(auth_bp)
