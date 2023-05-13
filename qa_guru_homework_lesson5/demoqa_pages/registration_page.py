import time

from selene import browser, have
from selene.core import command

from qa_guru_homework_lesson5 import resources


class RegistrationFormPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element( f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self
    def fill_user_email(self, email):
        browser.element('#userEmail').click().type(email)

    def select_gender(self):
        browser.element('[for="gender-radio-2"]').click()

    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)

    def select_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobby(self):
        browser.all('.custom-checkbox').element_by(have.text('Reading')).perform(command.js.scroll_into_view).click()

    def upload_file(self, file_name):
        browser.element('#uploadPicture').send_keys(resources.path(file_name))
        time.sleep(1)

    def fill_address(self, address):
        browser.element('textarea#currentAddress').type(address)

    def fill_state(self):
        browser.element('#state').click()
        browser.element('#react-select-3-option-2').click()

    def fill_city(self):
        browser.element('#city').click()
        browser.element('#react-select-4-option-0').click()

    def click_submit(self):
        browser.element('#submit').press_enter()

    def registered_user_data(self):
        return browser.element('.table').all('td').even

    def should_registered_user_with(self, full_name, email, gender,phone_number,birthday,subject,hobby,image,address,city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                birthday,
                subject,
                hobby,
                image,
                address,
                city,
            )
        )
        return self
