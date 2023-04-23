import time

from selene import browser,have, be
from selene.core import command



def test_practice_form():
    browser.open('/')
    browser.element('#firstName').click().type('Meerim')
    browser.element('#lastName').click().type('Sabyt')
    browser.element('#userEmail').click().type('skmeerim1999@gmail.com')
    browser.element(css_or_xpath_or_by=("label[for='gender-radio-2']")).click()
    browser.element('#userNumber').click().type('0554803097')
    browser.element('#dateOfBirthInput').click()
    browser.element(css_or_xpath_or_by=('[class="react-datepicker__year-select"]')).click()
    browser.element('[value="1999"]').click()
    browser.element(css_or_xpath_or_by=('[class="react-datepicker__month-select"]')).click()
    browser.element('[value="9"]').click()
    browser.element(css_or_xpath_or_by=('[class="react-datepicker__day react-datepicker__day--031 react-datepicker__day--weekend"]')).click()
    browser.element(css_or_xpath_or_by=('#subjectsInput')).click().type('Ma').press_enter()
    browser.element(css_or_xpath_or_by=("label[for='hobbies-checkbox-2']")).perform(command.js.scroll_into_view).click()
    browser.element('#uploadPicture').send_keys(r"C:\Users\skmee\PycharmProjects\qa_guru_homework_lesson5\image\totoro.jpg")
    browser.element('textarea#currentAddress').type("str Abd 123")
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
