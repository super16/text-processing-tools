from pydantic import BaseModel, Field
from typing import List


class CorpusBase(BaseModel):
    title: str = Field(description="Corpus title")


class CorpusItem(CorpusBase):
    id: int = Field(description="Corpus Id")

    class Config:
        orm_mode = True


class CorpusCreate(BaseModel):
    title: str = Field(description="Corpus title")

    class Config:
        schema_extra = {
            "example": {
                "title": "Brown Corpus"
            }
        }
        orm_mode = True


class Corpora(BaseModel):
    corpora: List[CorpusItem]

    class Config:
        schema_extra = {
            "example": {
                "corpora": [
                    {
                        "id": 1,
                        "title": "Brown Corpus",
                    },
                    {
                        "id": 2,
                        "title": "Enron Corpus",
                    }
                ]
            }
        }
        orm_mode = True
