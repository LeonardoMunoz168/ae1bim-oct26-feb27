from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Base SQLite
URL_BD = "sqlite:///veterinaria.db"

# Motor de conexión
engine = create_engine(URL_BD)

# Sesión
Session = sessionmaker(bind=engine)
session = Session()