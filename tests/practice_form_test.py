import os
import time

import allure
from selene import have, command, by


@allure.title("Successful fill form")
def test_practice_form(setup_browser):
    browser = setup_browser

    with allure.step("Open Registration Form"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    with allure.step("Fill the form"):
        browser.element('#firstName').type('Meerim')
        browser.element('#lastName').type('Sabyt')
        browser.element('#userEmail').click().type('skmeerim1999@gmail.com')
        browser.element('[for="gender-radio-2"]').click()
        browser.element('#userNumber').type('0554803097')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1999"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="9"]').click()
        browser.element('.react-datepicker__day--031').click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Reading")).click()
        #file_path = os.path.abspath(os.path.join('image', 'totoro.jpg'))
        #browser.element('#uploadPicture').send_keys(file_path)
        #time.sleep(2)
        browser.element('textarea#currentAddress').type("str Abd 123")
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').click()
        browser.element('#submit').press_enter()

    # THEN
    with allure.step("Check final result"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        #browser.all('.table-responsive td:nth-child(2)').should((have.texts('Meerim Sabyt',
                                                                            #'skmeerim1999@gmail.com',
                                                                            #'Female',
                                                                            #'0554803097',
                                                                            #'31 October,1999',
                                                                            #'Maths',
                                                                            #'Reading',
                                                                            #'totoro.jpg',
                                                                            #'str Abd 123',
                                                                            #'Haryana Karnal')))
