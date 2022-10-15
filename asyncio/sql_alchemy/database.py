from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class AsyncDatabaseSession:

    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        self._engine = create_async_engine(
            "postgresql+asyncpg://postgres_user:postgres_password@localhost/postgres_db",
            echo=True
        )

        self._session = sessionmaker(
            self._engine,
            expire_on_commit=False,
            class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)


async_db_session = AsyncDatabaseSession()
