# codeing:utf-8
from app.model import db
from sqlalchemy import UniqueConstraint
from datetime import datetime


class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    chapter = db.Column(db.Integer)
    text = db.Column(db.String(10000))
    created_time = db.Column(db.DateTime(), default=datetime.now)

    UniqueConstraint("title", "chapter", name="ui_tc")

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "chapter": self.chapter,
            "text": self.text,
        }
