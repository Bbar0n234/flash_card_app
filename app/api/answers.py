from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.models import Answers, db_helper
from core.schemas import AnswerUpdate, AnswerRead
from typing import List

router = APIRouter(tags=["Answers"])


@router.get("/", response_model=List[AnswerRead])
async def read_answers(session: AsyncSession = Depends(db_helper.session_getter)):
    result = await session.execute(select(Answers))
    answers = result.scalars().all()

    return answers


@router.get("/{user_card_id}", response_model=AnswerRead)
async def read_answer(user_card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    return answer


@router.delete("/{user_card_id}")
async def delete_answer(user_card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    await session.delete(answer)
    await session.commit()

    return {"detail": "Answer deleted"}


@router.patch("/{user_card_id}/increment_right", response_model=AnswerRead)
async def increment_right_answer(user_card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    answer.right_answers += 1

    await session.commit()
    await session.refresh(answer)

    return answer


@router.patch("/{user_card_id}/increment_wrong", response_model=AnswerRead)
async def increment_wrong_answer(user_card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    answer.wrong_answers += 1

    await session.commit()
    await session.refresh(answer)

    return answer


@router.patch("/{user_card_id}/reset", response_model=AnswerRead)
async def reset_answers(user_card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    answer.right_answers = 0
    answer.wrong_answers = 0

    await session.commit()
    await session.refresh(answer)

    return answer


@router.put("/{user_card_id}", response_model=AnswerRead)
async def update_answer(user_card_id: int, updated_answer: AnswerUpdate, session: AsyncSession = Depends(db_helper.session_getter)):
    answer = await session.get(Answers, user_card_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    for key, value in updated_answer.model_dump(exclude_unset=True).items():
        setattr(answer, key, value)

    await session.commit()
    await session.refresh(answer)

    return answer
