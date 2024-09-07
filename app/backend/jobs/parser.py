import asyncio
from typing import Generator
import aiohttp
from bs4 import BeautifulSoup as bs
from app.backend.db.models import City, Profession
from sqlalchemy import insert
from app.backend.db.config import async_session_maker


class JobsPars:
    url = (
        'https://base.garant.ru/70433916/'
        '53f89421bbdaf741eb2d1ecc4ddb4c33/'
    )

    @classmethod
    async def get_jobs(cls) -> Generator:
        async with aiohttp.ClientSession() as session:
            async with session.get(cls.url) as response:
                soup = bs(await response.text(), 'html.parser')
                cards = soup.find_all('tr')
                for card in cards:
                    title = card.find_next().find_next()\
                        .find_next().find_next().find_next()
                    yield title.text.lstrip().rstrip()

    @classmethod
    async def insert_in_table(cls) -> None:
        async for job in cls.get_jobs():
            async with async_session_maker() as session:
                await session.execute(
                    insert(Profession).values(title=job)
                )
                await session.commit()
        print('Все успешно сохранено')


class CityPars:
    url = (
        'https://ru.wikipedia.org/wiki/'
        '%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA'
        '_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2'
        '_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
    )

    @classmethod
    async def get_city(cls) -> Generator:
        async with aiohttp.ClientSession() as session:
            async with session.get(cls.url) as response:
                soup = bs(await response.text(), 'html.parser')
                cards = soup.find('tbody').find_all('tr')
                for card in cards:
                    title = card.find_next('td').find_next('td')\
                        .find_next('td').find('a')
                    yield title.text

    @classmethod
    async def insert_in_table(cls) -> None:
        async for city in cls.get_city():
            async with async_session_maker() as session:
                await session.execute(
                    insert(City).values(title=city)
                )
                await session.commit()
        print('Все успешно сохранено')


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(JobsPars.insert_in_table())
        # tg.create_task(CityPars.insert_in_table())


if __name__ == '__main__':
    asyncio.run(main())
