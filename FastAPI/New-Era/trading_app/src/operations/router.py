from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from operations.models import operation
from operations.schemas import OperationCreate

from database import get_async_session

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    queru = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(queru)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operations: OperationCreate, session: AsyncSession =  Depends(get_async_session)):
    stmt = insert(operation).values(**new_operations.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}