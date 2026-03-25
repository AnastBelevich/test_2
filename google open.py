from selene import browser, be, by


browser.open('https://google.com')
if browser.element(by.text('Принять все')).matching(be.visible):
   browser.element(by.text('Принять все')).click()
   browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
# browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))
