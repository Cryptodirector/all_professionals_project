from sqlalchemy import insert, select

from app.backend.db.models import (
    Users,
    NumberExecutor,
    Profession,
    City
)
from app.backend.db.config import async_session_maker
from app.backend.schemas.schema import (
    UsersInfo,
    UsersCity,
    UsersProf,
    UsersNumber
)


async def insert_user(
        user: UsersInfo,
        prof: UsersProf,
        city: UsersCity,
        number: UsersNumber
) -> UsersInfo:
    async with async_session_maker() as session:
        stmt = await session.execute(
            insert(Users).values(
                **user.dict(),
                **prof.dict(),
                **city.dict()
            ).returning(Users.id)
        )
        await session.execute(
            insert(NumberExecutor).values(
                number=number.number,
                id_users=stmt.scalar()
            )
        )
        await session.commit()
        return user


class Info:

    @classmethod
    async def get_city(cls):
        async with async_session_maker() as session:
            query = await session.execute(
                select(City)
            )
            return query.scalars().all()

    @classmethod
    async def get_prof(cls):
        async with async_session_maker() as session:
            query = await session.execute(
                select(Profession)
            )
            return query.scalars().all()
