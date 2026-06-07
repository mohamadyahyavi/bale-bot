from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import AsyncSessionLocal


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session