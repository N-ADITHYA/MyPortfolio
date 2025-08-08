from fastapi import FastAPI, Depends
from backend.schemas import PostCreate, CreateUser
from backend.database import session_local, engine
from backend import models
from sqlalchemy.orm import Session
from backend import getDeets
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "https://iadiee.live",
    "https://www.iadiee.live"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Or specify frontend URL like "http://localhost:5500"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/create_user", response_model=PostCreate)
def create_user(deets: CreateUser, db: Session = Depends(get_db)):
    return getDeets.entryDeets(db, deets)
