# esta configuracion debe ir en init.py

#configuracion de base de datos 
SQLITE = "sqlite:///project.db"  #       ojo con los  ⬇️ caracteres especiales
POSTGRESQL = "postgresql+psycopg2://postgres:joan501%40@localhost:5432/register_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    
    SQLALCHEMY_DATABASE_URI = POSTGRESQL