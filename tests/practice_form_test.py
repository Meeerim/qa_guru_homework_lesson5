from qa_guru_homework_lesson5.data.users import student
from qa_guru_homework_lesson5.demoqa_pages.registration_page import RegistrationFormPage


def test_practice_form():
    registration_page = RegistrationFormPage()
    registration_page.open()
    registration_page.fill_user_info(student)
    registration_page.click_submit()

    # THEN

    registration_page.should_registered_user_with('Meerim Sabyt',
                                                  'skmeerim1999@gmail.com',
                                                  'Female',
                                                  '0554803097',
                                                  '10 May,1999',
                                                  'Maths',
                                                  'Reading',
                                                  'totoro.jpg',
                                                  'str Abd 123',
                                                  'NCR Delhi')
