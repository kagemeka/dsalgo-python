import typing


def test() -> typing.NoReturn:
    a = [-1] * 5
    for i in a[::-1]:
        print(i)
        a[i - 1] += 1
        print(a)


if __name__ == '__main__':
    test()
