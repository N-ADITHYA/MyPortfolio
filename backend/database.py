from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


env_path = os.path.join(os.path.dirname(__file__), '.env')
env_path1 = os.path.join(os.path.dirname(__file__), '.env.test')#external DB
load_dotenv(dotenv_path=env_path)
load_dotenv(dotenv_path=env_path1)

if os.getenv("TESTING"):
    db_url = os.getenv("TEST_DATABASE_URI")
else:
    db_url = os.getenv("DATABASE_URI")
engine = create_engine(db_url)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



