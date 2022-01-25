import asyncio
import typing


class AsyncUnionFind:
    __data: typing.List[int]

    async def __init(self, size: int) -> None:
        self.__data = [-1] * size

    def __init__(self, size: int) -> None:
        # self.__data = [-1] * size
        # asyncio.get_event_loop().run_until_complete(self.__init(size))
        asyncio.create_task(self.__init(size))

    async def find(self, u: int) -> int:
        d = self.__data
        if d[u] < 0:
            return u
        d[u] = await self.find(d[u])
        return d[u]

    async def unite(self, u: int, v: int) -> asyncio.Future[None]:
        u, v = await self.find(u), await self.find(v)
        if u == v:
            return
        d = self.__data
        if d[u] > d[v]:
            u, v = v, u
        d[u] += d[v]
        d[v] = u


async def get_sum(n: int) -> int:
    s = 0
    for i in range(n):
        s += i
        print(s)
        await asyncio.sleep(0.00000001)
    print(f"done: {n}")
    return s


def gen():
    for i in range(10):
        yield i


def gen_multi():
    for _ in range(10):
        yield from gen()


for a in gen_multi():
    print(a)


async def main() -> None:
    # await get_sum(100000)
    # await get_sum(10000)
    # await get_sum(1000)

    # task1 = get_sum(100000)
    # task2 = get_sum(10000)
    # task3 = get_sum(1000)
    # await task1
    # await task2
    # await task3

    task1 = asyncio.create_task(get_sum(100000))
    for i in range(1, 5):
        print(i)
    task2 = asyncio.create_task(get_sum(10000))
    for i in range(5, 9):
        print(i)
    # task3 = asyncio.create_task(get_sum(1000))
    # await task1
    # await task2
    # await task3
    # print(1)
    # print(await task3)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    # asyncio.run(main())
