from sqlalchemy.orm import Session

from models import Corpus
from schemas import CorpusCreate, CorpusItem


def get_corpora(db: Session):
    return db.query(Corpus).all()

def get_corpus_by_title(db: Session, title: str):
    return db.query(Corpus).filter(Corpus.title == title).first()

def get_corpus_by_title_and_id(db: Session, title: str, id: int):
    return db.query(Corpus).filter(
        Corpus.title == title
    ).filter(Corpus.id == id).first()

def get_corpus_by_id(db: Session, id: int):
    return db.query(Corpus).filter(Corpus.id == id).first()

def update_corpus(db: Session, corpus: CorpusItem, new_title: str):
    db_corpus = db.query(Corpus).filter(Corpus.id == corpus.id).one_or_none()
    if db_corpus is None:
        return None
    db_corpus.title = new_title
    db.add(db_corpus)
    db.commit()
    db.refresh(db_corpus)
    return db_corpus

def create_corpus(db: Session, corpus: CorpusCreate):
    db_corpus = Corpus(title=corpus.title)
    db.add(db_corpus)
    db.commit()
    db.refresh(db_corpus)
    return db_corpus
