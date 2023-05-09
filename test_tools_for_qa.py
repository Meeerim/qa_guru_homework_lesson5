import os
import time
from selene import browser, have
from selene.core import command


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().type('Meerim')
    browser.element('#lastName').click().type('Sabyt')
    browser.element('#userEmail').click().type('skmeerim1999@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').click().type('0554803097')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1999"]').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="9"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').click().type('Ma').press_enter()
    time.sleep(1)
    browser.element("[for='hobbies-checkbox-2']").perform(command.js.scroll_into_view).click()
    file_path = os.path.abspath(os.path.join('image', 'totoro.jpg'))
    browser.element('#uploadPicture').send_keys(file_path)
    time.sleep(1)
    browser.element('textarea#currentAddress').type("str Abd 123")
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should((have.texts('Meerim Sabyt',
                                                                        'skmeerim1999@gmail.com',
                                                                        'Female',
                                                                        '0554803097',
                                                                        '31 October,1999',
                                                                        'Maths',
                                                                        'Reading',
                                                                        'totoro.jpg',
                                                                        'str Abd 123',
                                                                        'Haryana Karnal')))

