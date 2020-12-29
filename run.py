from app import db,app
from app.site.models import Post
from flask.cli import FlaskGroup


cli = FlaskGroup(True)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    post = Post(title="Hello World",description="testing from flask CLI",source="Asal")
    post.save()



    
if __name__ == '__main__':
    cli()
    # Add host=0.0.0.0 to access from docker or everywhere
    # app.run(port=5000, debug=True, host='0.0.0.0')