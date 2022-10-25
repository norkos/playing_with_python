from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AccountORM(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True)
    name = Column(String, index=False)


class AccountBase(BaseModel):
    name: str | None = None
    email: str | None = None


class Account(AccountBase):
    id: str

    class Config:
        orm_mode = True


def test_create_from_orm():
    orm = AccountORM(
        id='my_id',
        email='norkos@gmail.com',
        name='what'
    )

    pydantic_model = Account.from_orm(orm)
    assert pydantic_model.id == orm.id
