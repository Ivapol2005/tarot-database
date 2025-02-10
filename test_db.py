import asyncio
from database import engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def test_connection():
    async with AsyncSession(engine) as session:
        try:
            result = await session.execute(text('SELECT 1'))
            print("✅ Підключення до PostgreSQL успішне")
        except Exception as e:
            print(f"❌ Помилка підключення: {e}")

asyncio.run(test_connection())

