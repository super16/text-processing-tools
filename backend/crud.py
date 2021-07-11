from sqlalchemy.orm import Session

from models import Corpus


def get_corpora(db: Session):
    return db.query(Corpus).all()
