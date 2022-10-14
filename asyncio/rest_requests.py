import requests
import time
import asyncio
import aiohttp

import platform
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def getting_pokemons_sync_way(how_many: int) -> None:
    print('Getting pokemons in syn way')
    t0 = time.time()
    for number in range(1, how_many):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        response = requests.get(url)
        name = response.json()['name']
        #print(name)
    print('It took me %0.2f ms' % (1000 * (time.time() - t0)))


async def getting_pokemons_async_way(how_many: int) -> None:
    print('Getting pokemons in async way')
    t0 = time.time()
    async with aiohttp.ClientSession() as session:
        for number in range(1, how_many):
            async with session.get(f'https://pokeapi.co/api/v2/pokemon/{number}') as response:
                result = await response.json()
                name = result['name']
                #print(name)
    print('It took me %0.2f ms' % (1000 * (time.time() - t0)))

if __name__ == "__main__":
    getting_pokemons_sync_way(50)
    asyncio.run(getting_pokemons_async_way(50))
