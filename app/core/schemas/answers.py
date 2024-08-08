from pydantic import BaseModel
from typing import Optional

class AnswerBase(BaseModel):
    right_answers: Optional[int] = 0
    wrong_answers: Optional[int] = 0


class AnswerUpdate(AnswerBase):
    pass


class AnswerRead(AnswerBase):
    user_card_id: int
