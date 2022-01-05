from kgmk.scrape.lambda_driver\
    import (
        CreateLambdaDriver,
    )
from webdriver_manager.chrome import(
    ChromeDriverManager,
)


def main():
    p = '/usr/bin/google-chrome'
    m = ChromeDriverManager()
    fn = CreateLambdaDriver()
    fn(p, m.install())


if __name__ == '__main__':
    main()
