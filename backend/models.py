from sqlalchemy import Integer, String, Column, DateTime, Boolean
from datetime import datetime
from backend.database import Base
class ContactForm(Base):
    __tablename__ =  'ContactForm'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)