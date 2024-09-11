from flask import Blueprint, render_template, request, redirect, url_for
from app.book.forms import Form
from app.models import Book, db
from werkzeug.utils import secure_filename
import os


landing_blueprint = Blueprint('landing', __name__, template_folder='templates')
book_blueprint = Blueprint('book', __name__, template_folder='templates')

@landing_blueprint.route("/", endpoint="index")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@book_blueprint.route("<int:id>/show", endpoint="show")
def show(id):
    book = db.get_or_404(Book, id)
    return render_template("show.html", book=book)

@book_blueprint.route("<int:id>/delete", endpoint="delete")
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("landing.index"))

@book_blueprint.route("/form/add", endpoint="add", methods=['GET', 'POST'])
def add():
    form = Form()
    if form.validate_on_submit():
        image = form.image.data 
        if image:
            image_name = secure_filename(image.filename)
            image.save(os.path.join('static/images/', image_name))
        else:
            image_name = None

        data = dict(request.form)
        del data['csrf_token']
        del data['submit']
        data["cover_photo"] = image_name

        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("landing.index"))

    return render_template("add.html", form=form)

@book_blueprint.route("<int:id>/form/edit", endpoint="edit", methods=['GET', 'POST'])
def edit(id):
    book = db.get_or_404(Book, id)
    form = Form(obj=book)

    if form.validate_on_submit():

        if 'image' in request.files:
            image = form.image.data
            if image:
                image_name = secure_filename(image.filename)
                image.save(os.path.join('static/images/', image_name))
                book.cover_photo = image_name
        
        book.title = form.title.data
        book.number_of_pages = form.number_of_pages.data
        book.description = form.description.data
        db.session.commit()
        return redirect(url_for("landing.index"))
    
    return render_template("edit.html", form=form)

