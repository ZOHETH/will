from typing import List
import logging

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from app.db.session import SessionLocal, engine
from app.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# # Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

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
