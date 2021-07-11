from pydantic import BaseModel, Field
from typing import List


class CorpusBase(BaseModel):
    id: int = Field(description="Corpus Id")


class Corpus(CorpusBase):
    title: str = Field(description="Corpus title")


class Corpora(BaseModel):
    data: List[Corpus] = []

    class Config:
        schema_extra = {
            "example": {
                "data": [
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
