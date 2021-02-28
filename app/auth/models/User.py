from dataclasses import dataclass
from datetime import datetime
from flask_login import UserMixin
from app import db, login_manger


# Load_user
@login_manger.user_loader
def load_user(user_id):
    return User.query.get_or_404(int(user_id))

# @dataclass
# class Role(db.Model):
#     __tablename__ = "role"
#     role_id: int = db.Column(db.Integer, primary_key=True)
#     name: str = db.Column(db.String(128), nullable=False, unique=True)
#     description: str = db.Column(db.Text)

#     def save(self) -> None:
#         db.session.add(self)
#         db.session.commit()

#     def delete(self) -> None:
#         db.session.delete(self)
#         db.session.commit()


# roles_users = db.Table('roles_users',
#                        db.Column('user_id', db.Integer(),
#                                  db.ForeignKey('user.id')),
#                        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(80), default="User")
    confirmed_at = db.Column(db.DateTime())

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
