from flask import Blueprint, render_template, request, redirect, url_for, g, flash

from werkzeug.security import generate_password_hash, check_password_hash
from register import db
from .models import User


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        #creo la instancia de la clase user 
        user = User(username, email,  generate_password_hash(password))
        
        # debo hacer una consulta para que no se repita el user es
        error = None
        
        #realizo la consulta asi:
        validate_user = User.query.filter_by(email=email).first()
        if validate_user == None:
            db.session.add(user)
            db.session.commit()
            
            return 'registro completo'
        else:
            error = 'correo ya existe ingrese otro'
        flash(error)
            
        
    
    
    return render_template('register.html')