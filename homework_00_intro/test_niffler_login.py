import selene


def test_success_login():
    selene.browser.open("https://niffler.qa.guru")
    selene.browser.element('[id="username"]').type("stas")
    selene.browser.element('[id="password"]').type("12345")
    selene.browser.element('[id="login-button"]').click()

    selene.browser.element('[id="spendings"]').should(
        selene.have.text("History of Spendings")
    )
    selene.browser.quit()


def test_success_login_with_press_enter():
    selene.browser.open("https://niffler.qa.guru")
    selene.browser.element('[id="username"]').type("stas")
    selene.browser.element('[id="password"]').type("12345").press_enter()

    selene.browser.element('[id="spendings"]').should(
        selene.have.text("History of Spendings")
    )
    selene.browser.quit()


def test_wrong_credentials():
    selene.browser.open("https://niffler.qa.guru")
    selene.browser.element('[id="username"]').type("stas")
    selene.browser.element('[id="password"]').type(
        "12345sgsrgwr"
    ).press_enter()

    selene.browser.element('[class="form__error"]').should(
        selene.have.text("Bad credentials")
    )
    selene.browser.quit()
