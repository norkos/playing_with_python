from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from database import Base, async_db_session


class AsyncModel:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def get(cls, id: int):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls).
                where(cls.id == id).
                values(**kwargs).
                execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()


class User(Base, AsyncModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    tweets = relationship('Tweet')


class Tweet(Base, AsyncModel):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(ForeignKey("users.id"))
    data = Column(String)

    @classmethod
    async def filter_by_user_id(cls, user_id: int):
        query = select(cls).where(cls.user_id == user_id)
        result = await async_db_session.execute(query)
        return result.scalars().all()
