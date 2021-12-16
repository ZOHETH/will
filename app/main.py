from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from app.db.session import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tfmodels/", response_model=schemas.TFModel)
def create_user(tfmodel: schemas.TFModel, db: Session = Depends(get_db)):

    return crud.create_tfmodel(db=db, tfmodel=tfmodel)


@app.get("/tfmodels/", response_model=List[schemas.TFModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tfmodels = crud.get_tfmodels(db, skip=skip, limit=limit)
    return tfmodels
