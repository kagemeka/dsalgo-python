from kgmk.sushida import (
    Sushida,
    SushidaCfg,
)

from selenium.webdriver import(
    Chrome,
    ChromeOptions,
)
from webdriver_manager.chrome \
    import (
        ChromeDriverManager,
    )


def create_driver():
    opts = ChromeOptions()
    for opt in [
        '--no-sandbox',
        '--start-maximized',
    ]:
        opts.add_argument(opt)
    opts.headless = False
    manager = (
        ChromeDriverManager()
    )
    return Chrome(
        manager.install(),
        options=opts,
    )


def main():
    cfg = SushidaCfg()
    driver = create_driver()
    f = Sushida(cfg)
    f(driver)
    driver.close()


if __name__ == '__main__':
    main()
