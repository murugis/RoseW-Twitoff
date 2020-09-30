from flask import Flask
from .db_model import DB
def create_app():
    '''Create and configure an instance of our flask application''' 
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///twitoff.db'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    return app

