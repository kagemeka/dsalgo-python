from kgmk.etyping import (
    ETyping,
    ETypingCfg,
    Auth,
    PlayCfg,
    Category,
)
import time

import selenium
from selenium.webdriver import(
    Firefox,
    FirefoxOptions,
)


def create_driver():
    opts = FirefoxOptions()
    opts.headless = False
    return Firefox(
        options=opts,
    )


def main():
    auth = Auth(
        '',
        '',
    )
    play_cfg = PlayCfg(
        interval=3.0,
    )
    cfg = ETypingCfg(
        auth,
        play_cfg,
        Category.ROMA,
    )
    driver = create_driver()
    fn = ETyping(cfg)
    fn(driver)

    time.sleep(1)
    driver.close()


if __name__ == '__main__':
    main()
