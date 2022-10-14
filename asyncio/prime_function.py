import time
import asyncio


def prime(x: int) -> bool:
    return not any(x//i == x/i for i in range(x-1, 1, -1))


async def highest_prime_below(x: int) -> int | None:
    print('Searching for highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if prime(y):
            print('Highest prime below %d is %d' % (x, y))
            return y
        await asyncio.sleep(0.01)
    return None


async def main():
    t0 = time.time()
    await asyncio.wait([
        asyncio.create_task(highest_prime_below(100000)),
        asyncio.create_task(highest_prime_below(10000)),
        asyncio.create_task(highest_prime_below(1000))
    ])
    duration = 1000 * (time.time() - t0)
    print('It took me %.2f ms' % duration)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()

