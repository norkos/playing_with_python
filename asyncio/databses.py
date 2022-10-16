import sqlalchemy
from databases import Database
import platform
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


metadata = sqlalchemy.MetaData()

tweets = sqlalchemy.Table(
    'tweets',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column('text', sqlalchemy.String(length=50))
)

engine = create_engine('sqlite:///./sql_app.db', echo=True)
metadata.create_all(engine)

database = Database('sqlite+aiosqlite:///./sql_app.db')


async def process():
    await database.connect()

    # insert
    query = tweets.insert()
    values = {'text': 'my_simple_tweet'}
    await database.execute(query=query, values=values)
    await database.execute(query=query, values=values)
    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(process())

