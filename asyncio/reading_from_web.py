import asyncio
import platform
import httpx
import time
import pprint

pp = pprint.PrettyPrinter(indent=2)

links = ['recipes', 'easyrecipes', 'TopSecretRecipes']

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_the_content(url: str) -> list[tuple[str, int, str]]:
    r = httpx.get(url)
    results = []
    for record in r.json()['data']['children']:
        title = record['data']['title']
        score = record['data']['score']
        results.append((title, score))
    return results


def get_the_data() -> None:
    print('Getting data in sync way')
    t0 = time.time()
    result = {}
    for link in links:
        result[link] = get_the_content(f'https://www.reddit.com/r/{link}/top.json?sort=top&t=day&limit=5')
    print('It took %0.2f ms' % (1000 * (time.time() - t0)))
    pp.pprint(result)


async def get_the_content_in_async(session: httpx.AsyncClient, url: str) -> list[tuple[str, int, str]]:
    r = await session.get(url)
    results = []
    for record in r.json()['data']['children']:
        title = record['data']['title']
        score = record['data']['score']
        results.append((title, score))
    return results


async def get_the_data_in_async() -> None:
    print('Getting data in async way')
    t0 = time.time()
    tasks = []
    async with httpx.AsyncClient() as session:
        for link in links:
            tasks.append(
                asyncio.create_task(
                    get_the_content_in_async(session,
                    f'https://www.reddit.com/r/{link}/top.json?sort=top&t=day&limit=5')
                )
            )
        results = await asyncio.gather(*tasks)
    print('It took %0.2f ms' % (1000 * (time.time() - t0)))
    pp.pprint(results)

if __name__ == "__main__":
    get_the_data()
    asyncio.run(get_the_data_in_async())
