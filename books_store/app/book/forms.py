from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FileField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    number_of_pages = IntegerField("Number of Pages", validators=[DataRequired()])
    image = FileField("Image", validators=[DataRequired()])
    submit = SubmitField("Create Book")
