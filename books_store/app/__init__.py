from flask import Flask
from flask_migrate import Migrate
from app.config import productionConfig
from app.models import db
from app.book.views import landing_blueprint, book_blueprint  
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(productionConfig)
    
    db.init_app(app)  
    migrate = Migrate(app, db)  
    bootstrap = Bootstrap5(app)  

    app.register_blueprint(landing_blueprint, url_prefix="/")  
    app.register_blueprint(book_blueprint, url_prefix="/books")  

    return app
