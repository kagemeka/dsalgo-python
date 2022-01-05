import typing
import dataclasses
from pprint import pprint
from kgmk.jstage import (
    SendRequest,
)
from kgmk.jstage.paper import (
    Params,
    Parse,
)


def test() -> typing.NoReturn:
    p = Params(
        text='concrete',
        count=2,
    )
    res = SendRequest()(
        dataclasses.asdict(p),
    )
    res = Parse()(res)
    pprint(res)


if __name__ == '__main__':
    test()
