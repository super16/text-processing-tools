from sqlalchemy import Column, Integer, String

from database import Base


class Corpus(Base):
    __tablename__ = "corpora"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
