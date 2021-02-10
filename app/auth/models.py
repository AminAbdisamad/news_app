from dataclasses import dataclass
from datetime import datetime
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from app import db


# @dataclass
# class User(db.Model):
#     __tablename__ = 'user'
#     user_id: int = db.Column(db.Integer, nullable=False, primary_key=True)
#     username: str = db.Column(db.String(100))
#     email: str = db.Column(db.String(120), nullable=False, unique=True)
#     # role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'),
#     #                     nullable=False)
#     roles = db.relationship('Role',
#                             backref=db.backref('user', lazy='dynamic'))

#     created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
#     modified_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)

#     # def save(self) -> None:
#     #     db.session.add(self)
#     #     db.session.commit()

#     # def delete(self) -> None:
#     #     db.session.delete(self)
#     #     db.session.commit()


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


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
