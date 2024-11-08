# app/database.py

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import 
from sqlalchemy.orm import sessionmaker,declarative_base
# DATABASE_URL = "sqlite:///./application_packages.db"
eng=r'/Users/eshaan/Desktop/Dev/Trace/application_package/database.db'
DATABASE_URL = f"sqlite:///{eng}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()






def init_db():
    from .models import Package, PackageComponent

    Base.metadata.create_all(bind=engine)
