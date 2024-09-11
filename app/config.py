import os
class Config():
    SECRET_KEY=os.urandom(32)
    @staticmethod 
    def init_app():
        pass

class productionConfig(Config):
    debug=False
    SQLALCHEMY_DATABASE_URI = "postgresql://fayoum:iti@localhost:5432/iti_flask_library"