from dataclasses import dataclass
from datetime import datetime
from app import db
# from app.models.category import posts_by_category

# @dataclass
# class Base(db.Model):
#     # __abstract__ = True # We dont want SQLAlchemy to create table for this
#     id: int = db.Column(db.Integer, primary_key=True)
#     created_at: datetime= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     modified_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,onupdate=datetime.utcnow)

#     def save(self) ->None:
#         db.session.add(self)
#         db.session.commit()

#     def delete(self) ->None:
#         db.session.delete()


@dataclass
class Post(db.Model):
    __tablename__ = "post"
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.Text)
    source: str = db.Column(db.String(129), nullable=True)
    category: str = db.Column(db.String(129), nullable=True)
    created_at: datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at: datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
