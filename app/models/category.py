from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.orm import backref
from app import db 


# Association Table 
posts_by_category = db.Table('posts_by_category',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'),primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'),primary_key=True)
)
# Category Model
@dataclass
class Category(db.Model):
    __name__ = "category"
    id: int = db.Column(db.Integer, nullable=False,primary_key=True)
    name:str = db.Column(db.String(80), nullable=False)
    description:str = db.Column(db.Text)
    posts = db.relationship("Post",secondary=posts_by_category)
    created_at: datetime= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow,onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

