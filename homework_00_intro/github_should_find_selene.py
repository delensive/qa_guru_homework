import selene

selene.browser.open("https://github.com/search")
selene.browser.element('[aria-label="Search GitHub"]').type(
    "qa.guru"
).press_enter()
selene.browser.element('[data-testid="results-list"]').should(
    selene.have.text("QA.GURU")
)
