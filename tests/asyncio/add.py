import asyncio
import time


i = 0


async def add():
    global i
    for _ in range(10):
        i += 1
        await asyncio.sleep(1e-1)


async def main():
    print('hello')

    task1 = asyncio.create_task(
        add(),
    )
    task2 = asyncio.create_task(
        add(),
    )
    await task1
    await task2

    print(i)
    print('finished')


def test():
    asyncio.run(main())


if __name__ == '__main__':
    test()
