import httpx
import time
import pprint

pp = pprint.PrettyPrinter(indent=2)

links = ['recipes', 'easyrecipes', 'TopSecretRecipes']


def get_the_content(url: str) -> list[tuple[str, int, str]]:
    r = httpx.get(url)
    results = []
    for record in r.json()['data']['children']:
        title = record['data']['title']
        score = record['data']['score']
        results.append((title, score))
    return results


def get_the_data_in_sync_way() -> None:
    print('Getting data in sync way')
    t0 = time.time()
    result = {}
    for link in links:
        result[link] = get_the_content(f'https://www.reddit.com/r/{link}/top.json?sort=top&t=day&limit=5')
    print('It took %0.2f ms' % (1000 * (time.time() - t0)))
    pp.pprint(result)


if __name__ == "__main__":
    get_the_data_in_sync_way()