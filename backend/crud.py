from sqlalchemy.orm import Session

from models import Corpus
from schemas import CorpusCreate


def get_corpora(db: Session):
    return db.query(Corpus).all()


def create_corpus(db: Session, corpus: CorpusCreate):
    db_corpus = Corpus(title=corpus.title)
    db.add(db_corpus)
    db.commit()
    db.refresh(db_corpus)
    return db_corpus
