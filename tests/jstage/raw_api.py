import typing
import requests
import xmltodict
from pprint import pprint


# 'affil=%E4%BA%94%E6%B4%8B%E5%BB%BA%E8%A8%AD'


url = (
    'http://'
    'api.jstage.jst.go.jp/'
    'searchapi/do?'
    'service=3&'
    # f'keyword=床版'
    'affil=床版'
)

params = {
    'service': 3,
    'text': '床版',
}


def main() -> typing.NoReturn:
    res = requests.get(
        url,
    )
    requests.get(
        'http://'
        'api.jstage.jst.go.jp/'
        'searchapi/do',
        params=params,
    )

    res = xmltodict.parse(res.content)
    res = dict(**res)
    print(res.keys())
    res = res['feed']
    print({**res['link']})
    # pprint(res)
    print(res.keys())
    res = res['entry']
    # print(res.keys())

    print(len(res))
    # pprint(res)


if __name__ == '__main__':
    main()
