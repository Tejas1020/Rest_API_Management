from sqlalchemy.orm import Session
from datetime import datetime
import json
import models, schemas


# ------------------------
# User Operations
# ------------------------
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# ------------------------
# Event Operations
# ------------------------
def create_event(db: Session, event_data: schemas.EventCreate, user_id: int):
    db_event = models.Event(**event_data.dict(), owner_id=user_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    save_event_version(db, db_event.id, event_data.dict())
    return db_event


def update_event(db: Session, event_id: int, updated_data: schemas.EventUpdate, user_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not db_event:
        return None

    for key, value in updated_data.dict().items():
        setattr(db_event, key, value)

    db.commit()
    db.refresh(db_event)

    save_event_version(db, db_event.id, updated_data.dict())
    return db_event


def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not db_event:
        return False
    db.delete(db_event)
    db.commit()
    return True


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


def list_events(db: Session, user_id: int):
    return db.query(models.Event).filter(models.Event.owner_id == user_id).all()


# ------------------------
# Versioning Operations
# ------------------------
def save_event_version(db: Session, event_id: int, data: dict):
    version = models.EventVersion(
        event_id=event_id,
        version_data=json.dumps(data),
        timestamp=datetime.utcnow()
    )
    db.add(version)
    db.commit()


def get_event_versions(db: Session, event_id: int):
    return db.query(models.EventVersion).filter(models.EventVersion.event_id == event_id).order_by(models.EventVersion.timestamp.desc()).all()


def get_event_version_by_id(db: Session, version_id: int):
    return db.query(models.EventVersion).filter(models.EventVersion.id == version_id).first()


def rollback_event_to_version(db: Session, event_id: int, version_id: int):
    version = get_event_version_by_id(db, version_id)
    if not version:
        return None

    data = json.loads(version.version_data)
    updated_event = update_event(db, event_id, schemas.EventUpdate(**data), user_id=None)
    return updated_event
