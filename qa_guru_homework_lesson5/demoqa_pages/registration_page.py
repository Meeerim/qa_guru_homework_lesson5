import time

from selene import browser, have
from selene.core import command

from qa_guru_homework_lesson5 import resources
from qa_guru_homework_lesson5.data.users import User, Gender, Hobbies


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
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
                        ).click()
        return self

    def fill_user_email(self, email):
        browser.element('#userEmail').click().type(email)

    def select_gender(self, gender):
        if gender == Gender.MALE:
            browser.element('[for="gender-radio-1"]').click()
        elif gender == Gender.FEMALE:
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()


    def fill_user_number(self, number):
        browser.element('#userNumber').type(number)

    def select_subject(self,subject):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view).type(subject[0].value).press_enter()

    def select_hobby(self, hobby):
        if hobby == Hobbies.SPORTS:
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobby == Hobbies.READING:
            browser.element('[for="hobbies-checkbox-2"]').click()
        else:
            browser.element('[for="hobbies-checkbox-3"]').click()


    def upload_file(self, file_name):
        browser.element('#uploadPicture').send_keys(resources.path(file_name))
        time.sleep(1)

    def fill_address(self, address):
        browser.element('textarea#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(city)).click()

    def click_submit(self):
        browser.element('#submit').press_enter()

    def registered_user_data(self):
        return browser.element('.table').all('td').even

    def should_registered_user_with(self, full_name, email, gender, phone_number, birthday, subject, hobby, image,
                                    address, city):
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

    def fill_user_info(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_user_email(user.email)
        self.select_gender(user.gender)
        self.fill_user_number(user.user_number)
        self.fill_date_of_birth(user.birthday.year, user.birthday.month, user.birthday.day)
        self.select_subject(user.subject)
        self.select_hobby(user.hobby)
        self.upload_file(user.image)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
