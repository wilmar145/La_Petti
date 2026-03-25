from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Quita "TU_CONTRASEÑA" y deja los dos puntos seguidos de la arroba
URL_DATABASE = "mysql+pymysql://root:@localhost:3306/le_petit_cafe"

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()