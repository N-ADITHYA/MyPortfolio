from backend.schemas import CreateUser
from sqlalchemy.orm import Session
from backend import models

def entryDeets(db: Session, user: CreateUser):
    db_user = models.ContactForm(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user