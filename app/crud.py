from sqlalchemy.orm import Session

from . import models, schemas


def create_tfmodel(db: Session, tfmodel: schemas.TFModel):
    record = models.TFModel(**tfmodel.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_tfmodels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TFModel).offset(skip).limit(limit).all()
