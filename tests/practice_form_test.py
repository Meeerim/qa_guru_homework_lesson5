
from qa_guru_homework_lesson5.demoqa_pages.registration_page import RegistrationFormPage


def test_practice_form():
    registration_page = RegistrationFormPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Meerim')
    registration_page.fill_last_name('Sabyt')
    registration_page.fill_user_email('skmeerim1999@gmail.com')
    registration_page.select_gender()
    registration_page.fill_user_number('0554803097')
    registration_page.fill_date_of_birth('1999', 'October', '31')
    registration_page.select_subject('Ma')
    registration_page.select_hobby()
    registration_page.upload_file('totoro.jpg')
    registration_page.fill_address("str Abd 123")
    registration_page.fill_state()
    registration_page.fill_city()
    registration_page.click_submit()

    # THEN

    registration_page.should_registered_user_with('Meerim Sabyt',
                                                  'skmeerim1999@gmail.com',
                                                  'Female',
                                                  '0554803097',
                                                  '31 October,1999',
                                                  'Maths',
                                                  'Reading',
                                                  'totoro.jpg',
                                                  'str Abd 123',
                                                  'Haryana Karnal')
