import asyncio
from database import async_db_session
from models import Tweet, User
import platform

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def init_app():
    await async_db_session.init()
    await async_db_session.create_all()


async def create_user():
    await User.create(name="Norbert Jan")
    user = await User.get(1)
    return user.id


async def create_post(user_id, data):
    await Tweet.create(user_id=user_id, data=data)
    posts = await Tweet.filter_by_user_id(user_id)
    return posts


async def update_user(id, name):
    await User.update(id, name=name)
    user = await User.get(id)
    return user.name


async def async_main():
    await init_app()
    user_id = await create_user()
    await update_user(user_id, "Norbert Franciszek")
    await create_post(user_id, "Welcome")


asyncio.run(async_main())
