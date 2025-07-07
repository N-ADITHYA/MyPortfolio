from fastapi import FastAPI, Depends
from backend import schemas, models, getDeets, database

from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend URL like "http://localhost:5500"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_user", response_model=schemas.PostCreate)
def create_user(deets: schemas.CreateUser, db: Session = Depends(get_db)):
    return getDeets.entryDeets(db, deets)