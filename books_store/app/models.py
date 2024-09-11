from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Book(db.Model):
    __tablename__="book"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20))
    cover_photo=db.Column(db.String(50))
    number_of_pages=db.Column(db.Integer)
    description=db.Column(db.String(100))

    @property
    def image_url(self):
        return url_for ("static",filename=f"images/{self.cover_photo}")

    @property
    def show_url(self):
        return url_for ("book.show",id=self.id)
    @property
    def delete_url(self):
        return url_for ("book.delete",id=self.id)