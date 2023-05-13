from selene import browser


class SimpleUserRegistrationPage:
    def open(self):
        browser.open('/text-box')

    def fill_full_name (self,value):
        browser.element('#userName').type(value)

    def fill_email (self, email):
        browser.element('#userEmail').type(email)

    def fill_current_address (self,value):
        browser.element('#currentAddress').type(value)

    def fill_permanent_address(self,value):
        browser.element('#permanentAddress').type(value)
