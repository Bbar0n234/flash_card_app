from pydantic import BaseModel


class UserCardBase(BaseModel):
    user_id: int
    card_id: int


class UserCardCreate(UserCardBase):
    pass


class UserCardRead(UserCardBase):
    id: int


class UserCardUpdate(UserCardBase):
    pass
