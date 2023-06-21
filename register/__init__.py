from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
# instalarlo debe ser pip install Flask-SQLAlchemy


db= SQLAlchemy()




def create_app():
    
    app = Flask(__name__)
    
    @app.route('/exito')
    def exito():
        return render_template('exito.html')
    
    #registro los blueprints 
    from . import auth
    app.register_blueprint(auth.bp)
    
    app.config.from_object('config.Config')
    
    #configuracion db 
    db.init_app(app)
    
    
    from .models import User
    
    with app.app_context():
        db.create_all()
    
    return app