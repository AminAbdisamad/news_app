import click
from app import db, app
from app.auth.models import User, Role
from app.models.category import Category
from flask.cli import FlaskGroup


cli = FlaskGroup(True)


@cli.command("create_db")
@app.cli.command("create_db")
def create_db() -> None:
    db.drop_all()
    db.create_all()
    db.session.commit()


@app.cli.command("seed_db")
def seed_db() -> None:
    role = Role(name="User",
                description="User have super power")
    role.save()
    user = User(username="Geedi",
                email="geedi@test.com")
    user.save()


if __name__ == '__main__':
    cli()
    # Add host=0.0.0.0 to access from docker or everywhere
    # app.run(port=5001, debug=True, host='0.0.0.0')
