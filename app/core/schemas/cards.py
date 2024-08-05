from pydantic import BaseModel
from typing import Optional

class CardBase(BaseModel):
    english: str
    russian: str
    category_id: Optional[int] = None
    difficulty: Optional[int] = None

class CardRead(CardBase):
    id: int
    category_id: Optional[int] = None
    difficulty: Optional[int] = None

class CardCreate(CardBase):
    pass

class CardUpdate(CardBase):
    pass
