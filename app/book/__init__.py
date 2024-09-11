from flask import Blueprint
book_blueprint=Blueprint("book",__name__,url_prefix="/book")
landing_blueprint=Blueprint("landing",__name__,url_prefix="/")
from app.book import views
