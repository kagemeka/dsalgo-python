'''
reference 
https://www.youtube.com/watch?v=t5Bo1Je9EmE
'''


import asyncio
import time


async def foo(text: str):
    print(text)
    await asyncio.sleep(1)


async def main():
    print('hello')
    task = asyncio.create_task(
        foo('world'),
    )
    await asyncio.sleep(0.5)
    print('finished')


def test():
    asyncio.run(main())


if __name__ == '__main__':
    test()
