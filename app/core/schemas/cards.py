from pydantic import BaseModel
from typing import Optional

class CardBase(BaseModel):
    english: str
    russian: str

class CardRead(CardBase):
    id: int
    category: Optional[str] = None
    difficulty: Optional[str] = None

class CardCreate(CardBase):
    category: Optional[str] = None
    difficulty: Optional[str] = None

class CardUpdate(CardBase):
    category: Optional[str] = None
    difficulty: Optional[str] = None