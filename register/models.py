from register import db


# defino el modelo usuario

class User(db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String, nullable=False)
    
    #inicializo el objeto user con sus elementos
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def __repr__(self):
        return f'User: {self.username}' 