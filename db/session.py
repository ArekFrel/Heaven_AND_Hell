from db.credentials import password
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_connection_string = f"mysql+pymysql://root:{password}@localhost:3306/heaven_and_hell"

engine = create_engine(db_connection_string)


Session = sessionmaker(bind=engine)