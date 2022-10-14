import requests
import time
import asyncio


def getting_pokemons_sync_way(how_many: int) -> None:
    print('Getting pokemons in syn way')
    t0 = time.time()
    for number in range(1, how_many):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        response = requests.get(url)
        name = response.json()['name']
#        print(name)
    print('It took me %0.2f ms' % (1000 * (time.time() - t0)))


async def get_pokemon(id: int) -> None:
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    response = await requests.get(url)
    name = response.json()['name']


async def getting_pokemons_async_way(how_many: int) -> None:
    print('Getting pokemons in async way')
    t0 = time.time()
    tasks = []
    for number in range(1, how_many):
        tasks.append(asyncio.create_task(get_pokemon(number)))

    await asyncio.wait(tasks)
    print('It took me %0.2f ms' % (1000 * (time.time() - t0)))

if __name__ == "__main__":
    getting_pokemons_sync_way(50)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(getting_pokemons_async_way(50))
    loop.close()
